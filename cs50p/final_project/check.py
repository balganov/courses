import asyncio
import json

def main():
    # with open("vacancies.json", encoding="utf-8") as f:
    #     vacancies = json.load(f)

    # urls = [i["url"] for i in vacancies["items"][:5]]

    my_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

    for k in my_dict.keys():
        print(k)


main()
