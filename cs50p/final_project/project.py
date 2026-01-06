import json
import sys
import threading
import time
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF
import aiohttp
import asyncio

#global variable for loading thread
loading = True

def main():
    global loading

    # First we fetch dictionaries from corresponding endpoints and write them to local json flies
    asyncio.run(fetch_dictionaries())
    display_areas = '\n'.join(f"{e['id'].rjust(5)} {e['name']}" for e in get_areas())
    display_roles = '\n'.join(f"{e['id'].rjust(5)} {e['name']}" for e in get_roles())

    area_ids = validated_input(f"Available locations:\n{display_areas}\nPlease select your preferred work locations:", get_areas())
    role_ids = validated_input(f"Available professional roles:\n{display_roles}\nPlease specify the job roles you are seeking:", get_roles())

    asyncio.run(fetch_vacancies(role_ids, area_ids))

    #Creating a thread to animate the loading since our function takes some time to fetch data from multiple urls
    loading_thread = threading.Thread(target=loading_animation)
    loading_thread.start()
    try:
        data = get_summary()
    finally:
        loading = False
        loading_thread.join()

    #Here we create a two-dimensional plot that has 2 rows and 3 comlums resulting in 6 charts in total
    # r - rows, c - columns, n - iterator for setting the titles
    r, c, n = 2, 3, 0
    _, ax = plt.subplots(r,c, figsize=(20,12))
    colors = plt.get_cmap('viridis')(np.linspace(0.9, 0.4, len(data)))

    titles = ['Top 5 industries','Work format', 'Work experience', 'Top 5 cities', 'Professional roles', 'Type of employment']
    #Setting titles for each chart
    for i in range(r):
        for j in range(c):
            ax[i,j].set_title(titles[n], fontsize=20, fontweight='bold')
            n += 1

    #Generating pie charts located in the first row
    ax[0,0].pie(data[1].values(), labels=data[1].keys(), colors=colors, autopct='%.2f%%', textprops={'fontsize': 13})
    ax[0,1].pie(data[5].values(), labels=data[5].keys(), colors=colors, autopct='%.2f%%', textprops={'fontsize': 13})
    ax[0,2].pie(data[2].values(), labels=data[2].keys(), colors=colors, autopct='%.2f%%', textprops={'fontsize': 13})
    #Generating bar charts located in the second row
    ax[1,0].bar(data[0].keys(), data[0].values(), color=colors)
    ax[1,1].bar(data[3].keys(), data[3].values(), color=colors)
    ax[1,2].bar(data[4].keys(), data[4].values(), color=colors)

    #Adjusting font size for bar charts
    for i in range(3):
        ax[1,i].tick_params(axis='x', labelsize=12, rotation=45)

    #Fixing the layout, so labels don't overlap and then saving the charts to png file
    plt.tight_layout()
    plt.savefig("charts.png")

    #Here we count skills occurances from each vacancy URL, generate wordcloud and save it to png file
    count_skills = Counter(get_skills())
    wcloud = WordCloud(background_color='white', width=2000,height=1200).generate_from_frequencies(count_skills)
    wcloud.to_file("word_cloud.png")

    visualization_requested = input("Would you like to generate a visualization in the form of charts to summarize the data? (y/n):")
    if visualization_requested.lower() == 'y':
        generate_pdf("charts.png", "word_cloud.png")
    else:
        print("If you want to analyze other vacancies, please rerun the program. Thank you.")

    print("done")

def validated_input(prompt, values):
    valid_ids = set(int(e['id']) for e in values)
    while True:
        user_input = input(prompt)

        if not user_input:
            print("Error: Input cannot be empty.")
            continue

        try:
            selected_ids = [int(v.strip()) for v in user_input.split(',')]
            if all(i in valid_ids for i in selected_ids):
                return selected_ids
            else:
                print("Error: Please select only the IDs listed above.")
        except ValueError:
            print("Error: Please use only numbers and commas (e.g. 165 or 140, 2, 13)")


#Accessing roles and locations from dictionaries
async def fetch_dictionaries():
    semaphore = asyncio.Semaphore(2)
    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(fetch_one(session, 'https://api.hh.ru/professional_roles?locale=EN', semaphore))
            task2 = tg.create_task(fetch_one(session, 'https://api.hh.ru/areas?locale=EN', semaphore))

    roles = task1.result()
    areas = task2.result()

    with open("job_roles.json","w", encoding="utf-8") as f:
        json.dump(roles,f,indent=4, ensure_ascii=False)

    with open("areas.json", "w", encoding="utf-8") as f:
        json.dump(areas,f,indent=4, ensure_ascii=False)

    print("Fetching dictionaries ... done")

#Accessing list of vacancies filtered by location and roles
async def fetch_vacancies(role_params, area_params):
    header = {
        "User-Agent": "JobAnalyzer/1.0 (sdf010121@gmail.com)",
        "Authorization": f"Bearer APPLJFG7N22I3S8BBAE8ES7I573A8D4HBTF9P5FIQHNOJN12A5KGQ41VOLNI928K"
    }
    vacancy_params = {
        "professional_role":role_params,
        "area" : area_params,
        "clusters":"true",
        "per_page":"100",
        "locale": "EN",
        "page":0
        }

    # Collect the initial data
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get('https://api.hh.ru/vacancies', params=vacancy_params, headers=header) as response:
                print(f"Fetching vacancies, status: {response.status}")
                data = await response.json()

            pages = int(data["pages"])

            # Check if we have additional pages and append them to our existing data
            if pages > 1:
                for p in range(1, pages):
                    vacancy_params["clusters"] = "false"
                    vacancy_params["page"] = p
                    # vancancies = requests.get('https://api.hh.ru/vacancies', params=vacancy_params)
                    # data["items"].extend(vancancies.json()["items"])
                    async with session.get('https://api.hh.ru/vacancies', params=vacancy_params, headers=header) as response:
                        print(f"Fetching additional vacancies, status: {response.status}")
                        vac = await response.json()
                        data["items"].extend(vac["items"])

        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            print(f"Error fetching vacancies: {e}")

    # Write the collected data to a file
    with open("vacancies.json","w", encoding="utf-8") as f:
            json.dump(data,f,indent=4, ensure_ascii=False)

#Accessing individual vacancy information
async def fetch_descriptions(vacancies):
    results = []
    urls = [i["url"] for i in vacancies["items"]]
    total_urls = len(urls)
    REQ_PER_SECOND = 30

    # This implementation was simple, however very slow due to syncronious requests
    # try:
    #     print("Requesting data from API...", end='')
    #     for url in urls:
    #         r = requests.get(url)
    #         desc.append(r.json())
    # except requests.RequestException as e:
    #     sys.exit(e)

    print(f"Fetching {len(urls)} vacancy descriptions...")

    #fetching url batch based on api requirements - 30 requests per second
    semaphore = asyncio.Semaphore(REQ_PER_SECOND)
    async with aiohttp.ClientSession() as session:
        for i in range(0,total_urls,REQ_PER_SECOND):
            end = total_urls if total_urls-i < REQ_PER_SECOND else i+REQ_PER_SECOND
            tasks = [asyncio.create_task(fetch_one(session, url, semaphore)) for url in urls[i:end]]
            print(tasks)
            current_results = await asyncio.gather(*tasks)
            results.extend(current_results)

            if end < total_urls:
                print(f"Pausing for 1.2 seconds to meet API rate limits")
                await asyncio.sleep(1.2)

    print("Creating local JSON file with vacancy descriptions...")
    with open("vacancy_descriptions.json","w", encoding="utf-8") as f:
            json.dump(results,f,indent=4, ensure_ascii=False)

#Fetching one url for asynchronious requests
async def fetch_one(session, url, semaphore, param=None):
    header = {
        "User-Agent": "JobAnalyzer/1.0 (sdf010121@gmail.com)",
        "Authorization": "Bearer APPLJFG7N22I3S8BBAE8ES7I573A8D4HBTF9P5FIQHNOJN12A5KGQ41VOLNI928K"
    }
    async with semaphore:
        try:
            async with session.get(url, headers=header, params=param) as response:
                print(f"Fetching {response.url}, status: {response.status}")
                return await response.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            print(f"Error fetching {response.url}: {e}")

#Reading data from local JSON: list of roles
def get_roles():
    with open("job_roles.json", "r", encoding="utf-8") as f:
        job_roles = json.load(f)

    keys = ['id','name']
    list = job_roles["categories"][7]["roles"]
    return [{key: e[key] for key in keys} for e in list]
    #return '\n'.join(f"[{e['id']}]  {e['name']}" for e in job_roles["categories"][7]["roles"])

#Reading data from local JSON: list of locations
def get_areas():
    with open("areas.json", "r", encoding="utf-8") as f:
        areas = json.load(f)

    keys = ['id','name']
    areas = sorted(areas,key=lambda x: x['name'])
    return [{key: e[key] for key in keys} for e in areas if e['name'] != "Other regions"]
    #return '\n'.join(f"[{e['id']}]  {e['name']}" for e in areas if e['name'] != "Other regions")

#Reading data from local JSON: summarized data from clusters
def get_summary():
    summary = {}
    summary_list = []
    with open("vacancies.json", "r", encoding="utf-8") as f:
        vacancies = json.load(f)

    #Create local JSON file with vacancy descriptions
    asyncio.run(fetch_descriptions(vacancies))
    #Total number of vacancies
    #total = vacancies["found"]

    #Summary of regions, industries, work experience, roles, work format, employment type
    for i in range(len(vacancies["clusters"])):
        summary = {}
        if i in [0,2]:
            for c in vacancies["clusters"][i]["items"][:5]:
                summary.update({c['name']: c['count']})
            summary_list.append(summary)
        elif i in [3,5,8,11]:
            for c in vacancies["clusters"][i]["items"]:
                summary.update({c['name']: c['count']})
            summary_list.append(summary)

    print("\nSuccess!")

    return summary_list

#Extracting skills from each vacancy
#It will be useful for future extractions of data from a particular vacancy
def get_skills():
    skills = []
    counter = 0
    with open("vacancy_descriptions.json", "r", encoding="utf-8") as f:
        desc = json.load(f)

    for d in desc:
        if d["key_skills"] == []:
            counter += 1
        else:
            for i in d["key_skills"]:
                skills.append(i["name"])
    return skills

#Merging to images into one pdf
def generate_pdf(img1, img2):
    try:
        pdf = FPDF(orientation='P', format='A4', unit='mm')
        pdf.add_page()
        pdf.image(img1, w=190, keep_aspect_ratio=True)
        pdf.set_font("Helvetica", style="B", size=9)
        pdf.cell(0, 35, "Required skills (Word Cloud)", align="C")
        pdf.set_xy(10,0)
        pdf.image(img2, y=150, w=190, keep_aspect_ratio=True)
        pdf.output("summary.pdf")

    except FileNotFoundError:
            sys.exit("Input does not exist")

#Printing one dot at a time as a loading animation
def loading_animation():
    global loading
    time.sleep(1)
    while loading:
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)

if __name__ == "__main__":
    main()
