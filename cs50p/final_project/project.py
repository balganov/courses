import requests

def main():

    fetch_dictionaries()

    print("done")

def fetch_dictionaries():
    try:
        roles = requests.get('https://api.hh.ru/professional_roles')
        areas = requests.get('https://api.hh.ru/areas')

        with open("job_roles","w") as file:
            file.write(str(roles.json()))

        with open("areas", "w") as file:
            file.write(str(areas.json()))


    except requests.RequestException as e:
        print(e)


if __name__ == "__main__":
    main()
