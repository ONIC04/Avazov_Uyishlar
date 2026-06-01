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
# List ichida (kitob_nomi, janr) ko'rinishidagi tuple-lar bor. Har bir janr bo'yicha kitoblarni guruhlang.


def guruhlash(books: list):
    d = {}
    for i in books:
        kitob = i[0]
        janr = i[1]
        if janr not in d:
            d[janr] = []
        d[janr].append(kitob)
    for i in d:
        print(i +":")
        for j in d[i]:
            print("    " + j)
            
    
books = [
    ("O'tkan kunlar", "Roman"),
    ("Mehrobdan chayon", "Roman"),
    ("Shum bola", "Povest"),
    ("Alkimyogar", "Roman"),
    ("Boy va kambag'al", "Hikoya"),
    ("Urush va tinchlik", "Roman"),
    ("Kecha va kunduz", "Roman"),
    ("Yulduzli tunlar", "Povest"),
    ("Qorako'z Majnun", "Hikoya"),
    ("Qalb ko'zi", "Hikoya")
]
guruhlash(books)