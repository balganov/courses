import asyncio
import json

async def main():
    # with open("vacancies.json", encoding="utf-8") as f:
    #     vacancies = json.load(f)

    # urls = [i["url"] for i in vacancies["items"][:5]]
    print("start")
    await asyncio.create_task(cor_func(5))
    print("checkpoint1")
    await cor_func(3)
    print("checkpoint2")
    await task
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
