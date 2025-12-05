import requests


def main():
    try:
        r = requests.get('https://api.hh.ru/professional_roles')

    except requests.RequestException as e:
        print(e)

    job_roles = r.json()
    print(job_roles["categories"][i]["id"] == )


if __name__ == "__main__":
    main()
