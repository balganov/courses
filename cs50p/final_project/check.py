import asyncio
import json

async def main():
    # with open("vacancies.json", encoding="utf-8") as f:
    #     vacancies = json.load(f)

    # urls = [i["url"] for i in vacancies["items"][:5]]
    print("start")
    task1 = asyncio.create_task(cor_func(100))
    print("checkpoint2")
    await task1
    print("done")

async def cor_func(n):

    for k in range(n):
        print("hey")
        if k % 30 == 0:
            await asyncio.sleep(5)
            print("waiting for 5 second")

asyncio.run(main())
