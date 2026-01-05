import asyncio
import aiohttp
import json

async def main():
    REQ_PER_SECOND = 2
    urls = ['https://api.hh.ru/vacancies/128638284?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128600670?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/127949831?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/127253831?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/128652740?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128675781?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/128739986?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128548168?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/128734657?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128511589?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/128511589?locale=EN&host=hh.ru']
    total_urls = len(urls)
    print("start")
    results = []


    semaphore = asyncio.Semaphore(2)
    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            for i in range(0,total_urls,2):
                end = total_urls if total_urls-i < REQ_PER_SECOND else i+REQ_PER_SECOND
                tasks = [tg.create_task(fetch_one(session, url, semaphore)) for url in urls[i:end]]
                print(tasks)
                await asyncio.sleep(1)

    results = [task.result() for task in tasks]

    with open("results.json", "w", encoding='utf-8') as f:
         json.dump(results,f,indent=4, ensure_ascii=False)
         print("Results are in a local file now")

async def fetch_one(session, url, semaphore):
    header = {
        "User-Agent": "JobAnalyzer/1.0 (sdf010121@gmail.com)",
        "Authorization": "Bearer APPLJFG7N22I3S8BBAE8ES7I573A8D4HBTF9P5FIQHNOJN12A5KGQ41VOLNI928K"
    }
    async with semaphore:
        async with session.get(url, headers=header) as response:
                print(f"Fetching {url}, status: {response.status}")
                #await asyncio.sleep(1)
                #print(f"Finished fetching, waited for 1 second")
                return await response.json()

asyncio.run(main())
