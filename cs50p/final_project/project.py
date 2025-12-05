import requests


def main():


    job_roles = r.json()

    for i, c in enumerate(job_roles["categories"]):
        if c["id"] == "11":
            print(c["roles"])
            break

def fetch_dictionaries():
    try:
        roles = requests.get('https://api.hh.ru/professional_roles')
        currency


    except requests.RequestException as e:
        print(e)


if __name__ == "__main__":
    main()
