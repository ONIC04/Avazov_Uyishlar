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
# 0 va 1 lardan iborat matritsa berilgan. Funksiya har bir qatorda nechta 1 borligini hisoblab ro'yxat qaytarsin.

def aniqlash(l: list) -> list:
    l1 = []
    for i in l:
        s = 0
        for j in i:
            if j == 1:
                s += 1
        l1.append(s)
    return l1

l = [[1, 0, 1],
     [1, 1, 0],
     [0, 0, 1]
]
javob = aniqlash(l)
print(javob)
