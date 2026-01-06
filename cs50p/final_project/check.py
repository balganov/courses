import asyncio
import aiohttp
import json

async def main():
    REQ_PER_SECOND = 2
    urls = []
    total_urls = len(urls)
    print("start")
    results = []

    header = {
        "User-Agent": "JobAnalyzer/1.0 (sdf010121@gmail.com)",
        "Authorization": "Bearer APPLJFG7N22I3S8BBAE8ES7I573A8D4HBTF9P5FIQHNOJN12A5KGQ41VOLNI928K"
    }
    vacancy_params = {
        "locale": "EN",
        "host":"hh.ru"
        }

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
