import asyncio
import json

def main():
    with open("vacancies.json", encoding="utf-8") as f:
        vacancies = json.load(f)


    urls = [i["url"] for i in vacancies["items"][:5]]

def fetch_one():
    

main()
