import requests
import json
import sys
import re
import threading
import time
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

#global variable for loading thread
loading = True

def validated_input(input):
    
    return validated_list


def main():
    global loading
    # First we fetch dictionaries from corresponding endpoints and write them to local json flies
    fetch_dictionaries()
    role_params = input(f"Please specify the job roles you are seeking:\n{get_roles()}\n").split(",")
    area_params = input(f"Please select your preferred work locations:\n{get_areas()}\n").split(",")

    #fetch_vacancies(role_params, area_params)
    #fetch_vacancies(['165','164','156'], ['40'])
    print("start")

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
    _, ax = plt.subplots(r,c, figsize=(20,10))
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
        ax[1,i].tick_params(axis='x', labelsize=12)

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

#Accessing roles and locations from dictionaries
def fetch_dictionaries():
    try:
        roles = requests.get('https://api.hh.ru/professional_roles?locale=EN')
        areas = requests.get('https://api.hh.ru/areas?locale=EN')

        with open("job_roles.json","w", encoding="utf-8") as f:
            json.dump(roles.json(),f,indent=4, ensure_ascii=False)

        with open("areas.json", "w", encoding="utf-8") as f:
            json.dump(areas.json(),f,indent=4, ensure_ascii=False)

        print("fetching is done")

    except requests.RequestException as e:
        sys.exit(e)

#Accessing list of vacancies filtered by location and roles
def fetch_vacancies(role_params, area_params):
    try:
        vacancy_params = {
            "professional_role":role_params,
            "area" : area_params,
            "clusters":"true",
            "per_page":"100",
            "locale": "EN",
            "page":0
            }

        # Collect the initial data
        vacancies = requests.get('https://api.hh.ru/vacancies', params=vacancy_params)
        data = vacancies.json()
        pages = int(data["pages"])

        # Check if we have additional pages and append them to our existing data
        if pages > 1:
            for p in range(1, pages):
                vacancy_params["clusters"] = "false"
                vacancy_params["page"] = p
                vancancies = requests.get('https://api.hh.ru/vacancies', params=vacancy_params)
                data["items"].extend(vancancies.json()["items"])

        # Write the collected data to a file
        with open("vacancies.json","w", encoding="utf-8") as f:
              json.dump(data,f,indent=4, ensure_ascii=False)

    except requests.RequestException as e:
        sys.exit(e)

#Accessing individual vacancy information
def fetch_descriptions(vacancies):
    desc = []
    urls = []
    print("Extracting vacancy URLs...")
    for i in vacancies["items"]:
        urls.append(i["url"])
    try:
        print("Requesting data from API...")
        for url in urls:
            r = requests.get(url)
            desc.append(r.json())
    except requests.RequestException as e:
        sys.exit(e)
    print("Creating local JSON file with vacancy descriptions...")
    with open("vacancy_descriptions.json","w", encoding="utf-8") as f:
            json.dump(desc,f,indent=4, ensure_ascii=False)

#Reading data from local JSON: list of roles
def get_roles():
    with open("job_roles.json", "r", encoding="utf-8") as f:
        job_roles = json.load(f)

    return '\n'.join(f"[{e['id']}]  {e['name']}" for e in job_roles["categories"][7]["roles"])

#Reading data from local JSON: list of locations
def get_areas():
    with open("areas.json", "r", encoding="utf-8") as f:
        areas = json.load(f)

    areas = sorted(areas,key=lambda x: x['name'])
    return '\n'.join(f"[{e['id']}]  {e['name']}" for e in areas if e['name'] != "Other regions")

#Reading data from local JSON: summarized data from clusters
def get_summary():
    summary = {}
    summary_list = []
    with open("vacancies.json", "r", encoding="utf-8") as f:
        vacancies = json.load(f)

    #Create local JSON file with vacancy descriptions
    #fetch_descriptions(vacancies)
    #Total number of vacancies
    total = vacancies["found"]

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
        pdf.image(img2, y=130, w=190, keep_aspect_ratio=True)
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
