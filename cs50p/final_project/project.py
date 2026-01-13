import json
import sys
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF
import aiohttp
import asyncio
import os
from dotenv import load_dotenv

REQ_PER_SECOND = 30

async def main():
    #Loading the access token from .env
    load_dotenv()
    # Creating folders to save our data and summary
    os.makedirs("data", exist_ok=True)
    os.makedirs("summary", exist_ok=True)

    #Fetching dictionaries from corresponding endpoints and writing them to local json files
    async with aiohttp.ClientSession() as session:
        await fetch_dictionaries(session)
        display_areas = '\n'.join(f"{e['id'].rjust(5)} {e['name']}" for e in get_areas())
        display_roles = '\n'.join(f"{e['id'].rjust(5)} {e['name']}" for e in get_roles())

        area_ids = validated_input(f"\nAvailable locations:\n{display_areas}\nPlease select ID(s) of your preferred work location(s):", get_areas())
        role_ids = validated_input(f"\nAvailable professional roles:\n{display_roles}\nPlease specify ID(s) of the job role(s) you are seeking:", get_roles())

        #Fetching vacancies based on the user input (proffesional roles and locations) and and writing them to local json files
        await fetch_vacancies(session, role_ids, area_ids)

        #Fetching vacancy descriptions and summarizing the data
        data = await get_summary(session)

    titles = ['Top 5 cities', 'Top 5 industries', 'Work experience', 'Professional roles', 'Type of employment', 'Work format']
    for title, summary in zip(titles,data):
        print(f"{title}: ")
        for key, value in summary.items():
            print(f"\t{key}: {value}")

    count_skills = Counter(get_skills())
    top_10 = count_skills.most_common(10)
    print("Top 10 skills:")
    for skill, count in top_10:
        print(f"\t{skill}: {count}")

    visualization_requested = input("Would you like to generate a visualization in the form of charts to summarize the data? (y/n):")
    if visualization_requested.lower() == 'y':
        print("Creating a dashboard with our fetched data... ")
        create_dashboard(data)

        #Counting skills occurances from each vacancy URL and generating wordcloud and save it to png file
        print("Creating a wordcloud for the skills... ")
        wcloud = WordCloud(background_color='white', width=2000,height=1200).generate_from_frequencies(count_skills)
        wcloud.to_file("summary/word_cloud.png")
        print("Creating a PDF file with our data... ")
        generate_pdf("summary/charts.png", "summary/word_cloud.png")
    else:
        print("If you want to analyze other vacancies, please rerun the program. Thank you.")


def validated_input(prompt, values):
    valid_ids = set(int(e['id']) for e in values)
    while True:
        user_input = input(prompt)

        if not user_input:
            print("***\nError: Input cannot be empty.\n***")
            continue

        try:
            selected_ids = [int(v.strip()) for v in user_input.split(',')]
            if all(i in valid_ids for i in selected_ids):
                return selected_ids
            else:
                print("***\nError: Please select only the IDs listed above.\n***")
        except ValueError:
            print("***\nError: Please use only numbers and commas (e.g. 165 or 140, 2, 13)\n***")


#Accessing roles and locations from dictionaries
async def fetch_dictionaries(session):
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_one(session, 'https://api.hh.ru/professional_roles?locale=EN'))
        task2 = tg.create_task(fetch_one(session, 'https://api.hh.ru/areas?locale=EN'))

    roles = task1.result()
    areas = task2.result()

    with open("data/job_roles.json","w", encoding="utf-8") as f:
        json.dump(roles,f,indent=4, ensure_ascii=False)

    with open("data/areas.json", "w", encoding="utf-8") as f:
        json.dump(areas,f,indent=4, ensure_ascii=False)

    print("Fetching dictionaries ... done")

#Accessing list of vacancies filtered by location and roles
async def fetch_vacancies(session, role_params, area_params):

    vacancy_params = {
        "professional_role":role_params,
        "area" : area_params,
        "clusters":"true",
        "per_page":"100",
        "locale": "EN",
        "page":0
        }

    # Collecting the initial data
    task = asyncio.create_task(fetch_one(session, 'https://api.hh.ru/vacancies', vacancy_params))

    data = await task
    pages = int(data["pages"])

    # Checking if we have additional pages and appending them to our existing data
    if pages > 1:
        for p in range(1, pages):
            vacancy_params["clusters"] = "false"
            vacancy_params["page"] = p
            task = asyncio.create_task(fetch_one(session, 'https://api.hh.ru/vacancies', vacancy_params))
            vac = await task
            data["items"].extend(vac["items"])

    # Writing the collected data to a file
    with open("data/vacancies.json","w", encoding="utf-8") as f:
            json.dump(data,f,indent=4, ensure_ascii=False)

#Accessing individual vacancy information
async def fetch_descriptions(session, vacancies):
    results = []
    urls = [i["url"] for i in vacancies["items"]]
    total_urls = len(urls)

    # This implementation was simple, however very slow due to syncronious requests
    # try:
    #     print("Requesting data from API...", end='')
    #     for url in urls:
    #         r = requests.get(url)
    #         desc.append(r.json())
    # except requests.RequestException as e:
    #     sys.exit(e)

    print(f"Fetching {len(urls)} vacancy descriptions...")

    for i in range(0,total_urls,REQ_PER_SECOND):
        end = total_urls if total_urls-i < REQ_PER_SECOND else i+REQ_PER_SECOND
        tasks = [asyncio.create_task(fetch_one(session, url)) for url in urls[i:end]]
        current_results = await asyncio.gather(*tasks)
        results.extend(current_results)

        if end < total_urls:
            print("Pausing for 1.1 seconds to respect API rate limits")
            await asyncio.sleep(1.1)

    print("Creating local JSON file with vacancy descriptions...")
    with open("data/vacancy_descriptions.json","w", encoding="utf-8") as f:
            json.dump(results,f,indent=4, ensure_ascii=False)

#Fetching one url for asynchronious requests
async def fetch_one(session, url, param=None):
    header = {
        "User-Agent": "JobAnalyzer/1.0 (sdf010121@gmail.com)",
        "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}"
    }
    async with asyncio.Semaphore(REQ_PER_SECOND):
        try:
            async with session.get(url, headers=header, params=param) as response:
                print(f"Fetching {response.url}, status: {response.status}")
                return await response.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            print(f"Error fetching {response.url}: {e}")

#Reading data from local JSON: list of roles
def get_roles():
    with open("data/job_roles.json", "r", encoding="utf-8") as f:
        job_roles = json.load(f)

    keys = ['id','name']
    #list = job_roles["categories"][7]["roles"]
    for category in job_roles["categories"]:
        if category["name"] == "Information technology":
            list = category["roles"]

    return [{key: e[key] for key in keys} for e in list]
    #return '\n'.join(f"[{e['id']}]  {e['name']}" for e in job_roles["categories"][7]["roles"])

#Reading data from local JSON: list of locations
def get_areas():
    with open("data/areas.json", "r", encoding="utf-8") as f:
        areas = json.load(f)

    keys = ['id','name']
    areas = sorted(areas,key=lambda x: x['name'])
    return [{key: e[key] for key in keys} for e in areas if e['name'] != "Other regions"]
    #return '\n'.join(f"[{e['id']}]  {e['name']}" for e in areas if e['name'] != "Other regions")

#Reading data from local JSON: summarized data from clusters
async def get_summary(session):
    summary_list = []
    with open("data/vacancies.json", "r", encoding="utf-8") as f:
        vacancies = json.load(f)

    #Creating local JSON file with vacancy descriptions
    await fetch_descriptions(session, vacancies)

    #Summary of regions, industries, work experience, roles, work format, employment type
    for cluster in vacancies["clusters"]:
        summary = {}
        if cluster["name"] in ["Region", "Company branch"]:
            for element in cluster["items"][:5]:
                if len(element['name'].split(',')) > 2:
                    elements = ','.join(element['name'].split(',')[:2])
                    summary.update({elements: element['count']})
                else:
                    summary.update({element['name']: element['count']})
            summary_list.append(summary)
        elif cluster["name"] in ["Work experience", "Professional role", "Type of employment", "Work format"]:
            for element in cluster["items"]:
                summary.update({element['name']: element['count']})
            summary_list.append(summary)

    return summary_list

#Extracting skills from each vacancy
#It will be useful for future extractions of data from a particular vacancy
def get_skills():
    skills = []
    with open("data/vacancy_descriptions.json", "r", encoding="utf-8") as f:
        desc = json.load(f)

    for d in desc:
        for skill in d["key_skills"]:
            skills.append(skill["name"])

    return skills

def create_dashboard(data):
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
    pie_ind = [1,5,2]
    for j, ind in enumerate(pie_ind):
        ax[0,j].pie(data[ind].values(), labels=data[ind].keys(), colors=colors, autopct='%.2f%%', textprops={'fontsize': 13})
    #Generating bar charts located in the second row
    bar_ind = [0,3,4]
    for j, ind in enumerate(bar_ind):
        ax[1,j].bar(data[ind].keys(), data[ind].values(), color=colors)

    #Adjusting font size for bar charts
    for j in range(3):
        ax[1,j].tick_params(axis='x', labelsize=12, rotation=45)

    #Fixing the layout, so labels don't overlap and then saving the charts to png file
    plt.tight_layout()
    plt.savefig("summary/charts.png")

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
        pdf.output("summary/summary.pdf")
        print("Success! You can check the results in a local folder.")
    except FileNotFoundError as e:
        sys.exit(f"Input file does not exist: {e}")

if __name__ == "__main__":
    asyncio.run(main())
