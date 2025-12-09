import requests
import json
import spacy
import sys
import re
from collections import Counter

def main():

    # First we fetch dictionaries from corresponding endpoints and write them to local json flies
    # fetch_dictionaries()
    # role_params = input(f"Please specify the job roles you are seeking:\n{get_roles()}\n").split(",")
    # area_params = input(f"Please select your preferred work locations:\n{get_areas()}\n").split(",")

    #fetch_vacancies(role_params, area_params)
    #fetch_vacancies(['165','164','156'], ['40'])
    print(analyze_vacancies())
    get_skills()

    print("done")

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
        print(e)

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
        print(e)


def get_roles():
    with open("job_roles.json", "r", encoding="utf-8") as f:
        job_roles = json.load(f)

    return '\n'.join(f"[{e['id']}]  {e['name']}" for e in job_roles["categories"][7]["roles"])

def get_areas():
    with open("areas.json", "r", encoding="utf-8") as f:
        areas = json.load(f)

    areas = sorted(areas,key=lambda x: x['name'])
    return '\n'.join(f"[{e['id']}]  {e['name']}" for e in areas if e['name'] != "Other regions")

def analyze_vacancies():
    total = 0
    summary = []
    with open("vacancies.json", "r", encoding="utf-8") as f:
        vacancies = json.load(f)

    #print(f"Total number of vacancies: {vacancies["found"]}")
    total = vacancies["found"]

    for i in range(len(vacancies["clusters"])):
        if i in [0,2]:
            for c in vacancies["clusters"][i]["items"][:5]:
                summary.append({c['name']: c['count']})
            print("d1")
        elif i in [3,5,11]:
            for c in vacancies["clusters"][i]["items"]:
                print(f"{c['name']}: {c['count']}")
            print()

    return total, summary

    # for i in vacancies["items"]:
    #     urls.append(i["url"])

    # for url in urls:
    #     r = requests.get(url)
    #     desc.append(r.json())

    # with open("vacancy_desc.json","w", encoding="utf-8") as f:
    #         json.dump(desc,f,indent=4, ensure_ascii=False)

def get_skills():
    with open("vacancy_desc.json", "r", encoding="utf-8") as f:
        desc = json.load(f)

    skills = []
    counter = 0

    for d in desc:
        if d["key_skills"] == []:
            counter += 1
        else:
            for i in d["key_skills"]:
                skills.append(i["name"])

    # count_skills = Counter(skills)
    # print(count_skills, counter)

if __name__ == "__main__":
    main()
