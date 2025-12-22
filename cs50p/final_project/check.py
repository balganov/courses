import asyncio
import json

def main():
    with open("vacancies.json", encoding="utf-8") as f:
        vacancies = json.load(f)


    for i in vacancies["items"]:
        print(i["url"])

main()
