import asyncio
import json

async def main():
    # with open("vacancies.json", encoding="utf-8") as f:
    #     vacancies = json.load(f)

    # urls = [i["url"] for i in vacancies["items"][:5]]
    print("start")
    task1 = asyncio.create_task(cor_func(5))
    await task1
    print("checkpoint1")
    task2 = asyncio.create_task(cor_func(3))
    await task2
    print("checkpoint2")
    print("done")

async def cor_func(n):

    for _ in range(n):
        if n==5:
            print("hey")
            await asyncio.sleep(1)
        else:
            print("---")
            await asyncio.sleep(3)

asyncio.run(main())
