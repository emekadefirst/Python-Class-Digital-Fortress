# # def is_vowel():
# #     vowel = ["a", "e", "i", "o", "u"]
# #     user_input = input("Type in your word below\n_").lower().strip()
# #     for i in user_input:
# #         if i in vowel:
# #             return "This word has a vowel"

# #     return "There are no vowels in this word"


# # print(is_vowel())

# # from datetime import datetime

# # time = datetime.now()

# # valv = datetime.strptime()
# # print(valv)

# import calendar
# import zoneinfo
# import os
# from dotenv import load_dotenv

# load_dotenv()

# # cal = calendar.month('2024', '10')
# # zon = zoneinfo.ZoneInfo()
# # print(cal)

# surf = os.makedirs('sule_daniel', exist_ok=True)
# all_dir = os.listdir('sule_daniel')
# # print(all_dir)
# home_dir = os.environ.get("YOTUBE_API")

# path = os.path.join("Document", "example.txt", home_dir)
# print("Path:", path)

import sys
import asyncio

async def charge(signal):
    while True:
        if signal != True:
            sys.exit()
        await light_up("Street_light")
async def light_up(bulb):
    while True:
        if bulb == True:
            print("Bulb is on")
            break

 