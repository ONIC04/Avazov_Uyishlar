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
# Talabalar baholari dict ko'rinishida berilgan: {ism: baho}. Funksiya baholarga qarab guruhlab, {baho: [ism1, ism2...]} ko'rinishida yangi dict qaytarsin.

def aniqlash(d: dict) -> dict:
    d1 = {}
    for i in d:
        b = d[i]
        d1[b] = []
    for i in d:
        b = d[i]
        k = i
        d1[b] = d1[b] + [k]
    return d1

d = {'Ali': 5, 'Vali': 4, 'Gulnoza': 5}
javob = aniqlash(d)
print(javob)
