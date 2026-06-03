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
# dict ko'rinishida telefon kitobi berilgan: {ism: raqam}. Funksiya ismni qabul qilib, raqamni qaytarsin. Agar topilmasa "Topilmadi" deb qaytarsin.


def aniqlash(kitob: dict, ism: str):
    r = ""
    t = 0
    for i in kitob:
        if i == ism:
            r = kitob[i]
            t = 1
            return r
    if t == 0:
        r = "Topilmadi"
        return r
        
        
kitob = {'Ali': '998901234567', 'Gulnoza': '998935678901'}
ism = input("Ism kiriting: ")
javob = aniqlash(kitob, ism)
print(javob)