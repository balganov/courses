import asyncio
import json

async def main():
    # with open("vacancies.json", encoding="utf-8") as f:
    #     vacancies = json.load(f)

    # urls = [i["url"] for i in vacancies["items"][:5]]
    print("HI")
    cor = cor_func(5)
    task = asyncio.create_task(cor)
    #asyncio.run(task)
    print("done")

async def cor_func(n: int = 1):

    for _ in range(n):
        print("hey")
        await asyncio.sleep(1)

asyncio.run(main())
