import asyncio
import json

def main():
    # with open("vacancies.json", encoding="utf-8") as f:
    #     vacancies = json.load(f)

    # urls = [i["url"] for i in vacancies["items"][:5]]
    gen()

def gen():
    print("hello")
    n=0
    while n < 10:
        yield n += 1
    print("world")

# asyncio.run(main())
main()
