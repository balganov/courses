import asyncio

def main():
    fetch()

def fetch():
    for i in range(10):
        print(i)
        asyncio.sleep(0.5)

main()
