import asyncio
import json

async def main():
    # with open("vacancies.json", encoding="utf-8") as f:
    #     vacancies = json.load(f)

    # urls = [i["url"] for i in vacancies["items"][:5]]
    print("hello")
    await asyncio.sleep(3)
    print("world")

asyncio.run(main())
