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
# Email nomi yaroqli ekanini tekshiruvchi funksiya yozing. Funksiya parametriga string turida email nomi kiritiladi, funksiya boolean qiymat qaytaradi.
# 	- Alfabitdagi katta va kichik harflar [A - Z], [a - z]
# 	- raqamlar [0 - 9] (majburiy emas)
# 	- "_" (pastki chiziq), "." (nuqta), "@" (kuchukcha belgisi)
# 	- "@" belgisida oldin doim qandaydir matn bo'lishi kerak
def aniqlash(s: str):
    l = []
    l1 = s.split("@")
    for i in range(len(s)):
        l.append(s[i])
    for i in range(len(l)-2, 0, -1):
        if l[i] == " ":
            return False
    if s.isdigit():
        print("Kiritilgan gmailda [A - Z], [a - z] Yo'q")  
    if "@" not in l:
        return False
    if len(l1[0]) == 0:
        return False
    bordomain = [
    "gmail.com", 
    "yahoo.com",
    "outlook.com", 
    "hotmail.com", 
    "live.com",
    "icloud.com", 
    "me.com",
    "mail.ru", 
    "bk.ru", 
    "inbox.ru", 
    "yandex.ru", 
    "ya.ru",
    "proton.me", 
    "protonmail.com", 
    "zoho.com", 
    "aol.com"
]
    belgi = ["_", "."]
    if l1[1] not in bordomain:
        return False
    for i in range(len(l1[0])):
        if not (l1[0][i].isalnum() or l1[0][i] in belgi):
            return False
    return True

s = input("Gmail manzil kiritng: ")
javob = aniqlash(s)
print(f"{javob}")
    

