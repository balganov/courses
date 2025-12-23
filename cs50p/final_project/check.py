import asyncio
import aiohttp
import json

async def main():

    urls = ['https://api.hh.ru/vacancies/128638284?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128600670?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/127949831?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/127253831?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/128652740?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128675781?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/128739986?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128548168?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/128734657?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128511589?locale=EN&host=hh.ru']

    print("start")
    results = []

    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            for url in urls:
                 tasks = tg.create_task(fetch_one(session, url))

    for task in tasks:
        results.append(task)

    with open("results.json", "w", encoding='utf-8') as f:
         json.dump(results,f,indent=4, ensure_ascii=False)

async def fetch_one(session, url):
    async with session.get(url) as response:
            print(f"Fetching {url}, status: {response.status}")
            return await response.json()

async def cor_func(n):

    for k in range(n):
        print("hey")
        if (k+1) % 2 == 0:
            await asyncio.sleep(1.1)
            print("waiting for 1.1 seconds")

asyncio.run(main())
