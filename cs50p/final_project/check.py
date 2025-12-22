import asyncio
import json

async def main():
    # with open("vacancies.json", encoding="utf-8") as f:
    #     vacancies = json.load(f)

    # urls = [i["url"] for i in vacancies["items"][:5]]
    await fetch_one()

async def fetch_one():

    for _ in range(5):
        print("fetching one URL")
        await asyncio.sleep(5)


await main()
