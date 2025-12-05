import requests
import json
from deep_translator import GoogleTranslator

def main():

    # First we fetch dictionaries from corresponding endpoints and write them to local json flies
    #fetch_dictionaries()
    print(f"Please select the roles that you are interested in:\n\n{get_roles()}")
    print("done")

def fetch_dictionaries():
    try:
        roles = requests.get('https://api.hh.ru/professional_roles')
        areas = requests.get('https://api.hh.ru/areas')

        with open("job_roles.json","w", encoding="utf-8") as f:
            json.dump(roles.json(),f,indent=4, ensure_ascii=False)

        with open("areas.json", "w", encoding="utf-8") as f:
            json.dump(areas.json(),f,indent=4, ensure_ascii=False)

    except requests.RequestException as e:
        print(e)

def get_roles():
    with open("job_roles.json", "r", encoding="utf-8") as f:
        job_roles = json.load(f)

    return GoogleTranslator(source="ru", target="en").translate('\n'.join(f"{i+1} {c['name']}" for i, c in enumerate(job_roles["categories"][7]["roles"])))

#def get_areas():


if __name__ == "__main__":
    main()
