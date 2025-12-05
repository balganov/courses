import requests


def main():
    try:
        r = requests.get('https://api.hh.ru/professional_roles')

    except requests.RequestException as e:
        print(e)

    job_roles = r.json()
    for i, c enumerate(job_roles["categories"]):
        if c["id"] == 11:
            print(i)



if __name__ == "__main__":
    main()
