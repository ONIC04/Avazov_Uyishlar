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
# [mahsulot_nomi, [narx1, narx2, ...]] ko'rinishidagi ro'yxatdan mahsulotlarning eng arzon narxni topadigan funksiya yozing.

def aniqlash(l: list) -> list:
    l1 = []
    for i in l:
        l1.append([i[0], min(i[1])])
    return l1

l = [['Olma', [12000, 11000, 11500]], ['Banan', [13000, 12500]]]
javob = aniqlash(l)
print(javob)