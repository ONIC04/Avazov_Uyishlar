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
#  Lug'atda mahsulot nomi va narxlari bor ({"olma": [1200, 1300, 1100], ...}). Har bir mahsulotning o'rtacha narxini chiqaruvchi funksiya yozing.

def urtacha(d: dict):
    l = []
    for i in d:
        y = sum(d[i])/len(d[i])
        l.append([i, y])
    d1 = dict(l)
    for i in d1:
        print(f"{i}: {d1[i]}")
        

d = {
    "olma": [13000, 14000, 15000],
    "anor": [19000, 22000, 24000, 15000],
    "gilos": [6000, 9000, 5000, 4000],
    "banan": [30000, 28000]
}
urtacha(d)