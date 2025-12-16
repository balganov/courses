import asyncio
import time

def main():
    fetch()

def fetch():
    for i in range(10):
        print(i)
        time.sleep(0.5)

main()
