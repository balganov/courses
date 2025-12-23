import asyncio
import json

async def main():
    with open("vacancies.json", encoding="utf-8") as f:
        vacancies = json.load(f)

    urls = [i["url"] for i in vacancies["items"][:10]]

    print("start")
    task1 = asyncio.create_task(cor_func(10))
    print("checkpoint2")
    await task1
    print("done")

async def cor_func(n):

    for k in range(n):
        print("hey")
        if (k+1) % 2 == 0:
            await asyncio.sleep(1.1)
            print("waiting for 1.1 seconds")

asyncio.run(main())
