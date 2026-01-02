import asyncio
import aiohttp
import json

async def main():
    RATE_LIMIT = 2
    urls = ['https://api.hh.ru/vacancies/128638284?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128600670?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/127949831?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/127253831?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/128652740?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128675781?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/128739986?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128548168?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/128734657?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128511589?locale=EN&host=hh.ru']

    print("start")
    results = []

    semaphore = asyncio.Semaphore(2)
    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            for start in range(0,len(urls),2):
                end = start if len(urls)-RATE_LIMIT < RATE_LIMIT
                tasks = [tg.create_task(fetch_one(session, url, semaphore)) for url in urls[start:batch+RATE_LIMIT]]
                print(tasks)
                await asyncio.sleep(5)

    results = [task.result() for task in tasks]

    with open("results.json", "w", encoding='utf-8') as f:
         json.dump(results,f,indent=4, ensure_ascii=False)
         print("Results are in a local file now")

async def fetch_one(session, url, semaphore):
    async with semaphore:
        async with session.get(url) as response:
                print(f"Fetching {url}, status: {response.status}")
                #await asyncio.sleep(1)
                #print(f"Finished fetching, waited for 1 second")
                return await response.json()

asyncio.run(main())
