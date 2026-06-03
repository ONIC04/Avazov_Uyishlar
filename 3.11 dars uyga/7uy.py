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
# Mahsulotlar list ko'rinishida berilgan: [{nom: ..., narx: ..., tur: ...}, ...].
# Funksiya narxi 10000 dan kam va turi "ichimlik" bo'lgan mahsulotlarni ajratsin.

def aniqlash(d: dict):
    l = []
    for i in d:
        if i["narx"] < 10000 and i["tur"] == "ichimlik":
            l.append(i)
            print(i)
    print("\n\n\n\n\n")
    
    print(l)

d = [
  {'nom': 'Cola',
   'narx': 9000, 
   'tur': 'ichimlik'
   },
  {'nom': 'Non',
   'narx': 3000,
   'tur': 'ovqat'
   },
  {'nom': 'Suv',
   'narx': 5000,
   'tur': 'ichimlik'
   }
]
aniqlash(d)


