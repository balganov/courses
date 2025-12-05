import requests
import json

def main():

    # First we fetch dictionaries from corresponding endpoints and write them to local json flies
    #fetch_dictionaries()
    get_roles()
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

        print(job_roles)

if __name__ == "__main__":
    main()
