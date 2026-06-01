#import math
#import requests
#import random
#import datetime
#import os, sys
#import time
#import pytz
#import json
# from deep_translator import GoogleTranslator as tarjimon
#from collections import Counter, defaultdict
print('\033[2J\033[3J\033[H', end='')
# List ichida turli ism-familiyalar bor. Shu listdan erkaklarni alohida, ayollarni alohida listlarga ajratib bering.
# (Farqlashda familyalardan foydalaning, erkaklarda "ov","ev", ayollarda "va" bilan tugaudi)

def ajrat(users: list) -> list:
    erkak = []
    ayol = []
    for i in users:
        l = i.split()
        familiya = l[1]
        y = familiya[-2:]
        if y == "ov" or y == "ev":
            erkak.append(i)
        elif y == "va":
            ayol.append(i)

    print(f"Erkaklar: {erkak}")
    print(f"Ayollar:  {ayol}")
    
users = [
    'Abdulla Abdullaev', 
    'Samandar Asadov', 
    'Shaxnoza Jurayeva', 
    'Ikrom Karimov',
    'Gulnora Xalilova',
    'Ziyoda Yuldashova'
    ]

ajrat(users)