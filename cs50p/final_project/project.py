import requests
import json

def main():

    fetch_dictionaries()

    print("done")

def fetch_dictionaries():
    try:
        roles = requests.get('https://api.hh.ru/professional_roles')
        areas = requests.get('https://api.hh.ru/areas')

        with open("job_roles.json","w") as f:
            json.dump(roles.json(),f,indent=4)

        with open("areas.json", "w") as f:
            json.dump(areas.json(),f,indent=4)


    except requests.RequestException as e:
        print(e)


if __name__ == "__main__":
    main()
