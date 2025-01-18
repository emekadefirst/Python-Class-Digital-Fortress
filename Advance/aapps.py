import time
import threading
import asyncio
import requests


# url = ["https://www.arise.tv/", "https://www.tvcnews.tv/", "https://www.channelstv.com/"]

# async def fetch_data(url):
#     response = requests.get(url)
#     # await asyncio.sleep(5)
#     print(response.status_code)


# async def main():
#     urls = ["https://www.arise.tv/", "https://www.tvcnews.tv/", "https://www.channelstv.com/"]
#     task = [fetch_data(url) for url in urls]

#     result = await asyncio.gather(*task)
#     print("result:", result)

# asyncio.run(main())


def type_numbers():
    for i in range(6):
        print(i)

def type_letters():
    for x in ['a', 'b', 'c', 'd', 'e', 'f']:
        print(x)



task_1 = threading.Thread(target=type_numbers)
task_2 = threading.Thread(target=type_letters)

event = threading.Event(target=task_1)
event.run()
print(event)