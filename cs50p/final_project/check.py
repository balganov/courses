import asyncio
import json

async def main():
    with open("vacancies.json", encoding="utf-8") as f:
        vacancies = json.load(f)

    urls = [i["url"] for i in vacancies["items"][:10]]

    print("start")
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(cor_func(10))
        task2 = tg.create_task(cor_func(5))
        print("checkpoint2")

    print("done")

async def cor_func(n):

    for k in range(n):
        print("hey")
        if (k+1) % 2 == 0:
            await asyncio.sleep(1.1)
            print("waiting for 1.1 seconds")

asyncio.run(main())
