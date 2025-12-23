import asyncio
import aiohttp
import json

async def main():

    urls = ['https://api.hh.ru/vacancies/128638284?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128600670?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/127949831?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/127253831?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/128652740?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128675781?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/128739986?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128548168?locale=EN&host=hh.ru',
            'https://api.hh.ru/vacancies/128734657?locale=EN&host=hh.ru', 'https://api.hh.ru/vacancies/128511589?locale=EN&host=hh.ru']

    print(urls)
    print("start")
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(cor_func(1))
        task2 = tg.create_task(cor_func(1))
        print("checkpoint2")

    print("done")

    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.hh.ru/vacancies/128638284?locale=EN&host=hh.ru') as response:
            print(response.status)
            print(await response.json())


async def cor_func(n):

    for k in range(n):
        print("hey")
        if (k+1) % 2 == 0:
            await asyncio.sleep(1.1)
            print("waiting for 1.1 seconds")

asyncio.run(main())
