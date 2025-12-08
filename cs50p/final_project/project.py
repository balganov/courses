import requests
import json

def main():

    # First we fetch dictionaries from corresponding endpoints and write them to local json flies
    # fetch_dictionaries()
    # role_params = input(f"Please specify the job roles you are seeking:\n{get_roles()}\n").split(",")
    # area_params = input(f"Please select your preferred work locations:\n{get_areas()}\n").split(",")

    # fetch_vacancies(role_params, area_params)
    analyze_vacancies()

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
            "locale": "EN"
            }

        print(vacancy_params)

        vacancies = requests.get('https://api.hh.ru/vacancies', params=vacancy_params)
        print(vacancies.url)

        pages = int(vacancies.json()["pages"])
        print(f"Total: {vacancies['found']} Pages: {pages}")

        if pages > 1:
            for p in range(pages):
                

        with open("vacancies.json","w", encoding="utf-8") as f:
             json.dump(vacancies.json(),f,indent=4, ensure_ascii=False)

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
    with open("vacancies.json", "r", encoding="utf-8") as f:
        vacancies = json.load(f)




if __name__ == "__main__":
    main()
