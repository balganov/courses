import requests


def main():
    try:
        r = requests.get('https://api.hh.ru/professional_roles')

    except requests.RequestException as e:
        print(e)

    vacancies = r.json()
    print(vacancies)

if __name__ == "__main__":
    main()
