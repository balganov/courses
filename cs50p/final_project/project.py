import requests

job_roles = {}
countries = {}

def main():

    fetch_dictionaries()

    for i, c in enumerate(job_roles["categories"]):
        if c["id"] == "11":
            print(c["roles"], i)
            break

def fetch_dictionaries():
    try:
        roles = requests.get('https://api.hh.ru/professional_roles')
        areas = requests.get('https://api.hh.ru/areas')

        job_roles = roles.json()
        countries = areas.json()

    except requests.RequestException as e:
        print(e)


if __name__ == "__main__":
    main()
