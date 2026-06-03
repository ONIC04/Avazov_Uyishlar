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
# Har bir talaba uchun [ism, [baholar]] ko'rinishidagi list berilgan. Funksiya yozing, u har bir talabaning o'rtacha bahosini hisoblab, [ism, o'rtacha_baho] ro'yxatini qaytarsin

def aniqlash(l: list) -> list:
    l1 = []
    
    for i in l:
        y = 0
        for j in i[1]:
            y = y + j
        u = y/len(i[1])
        l1.append([i[0], round(u, 2)])
    return l1
        
l = [['Ali', [5, 4, 3]], ['Gulnoza', [4, 4, 5]]]
javob = aniqlash(l)
print(javob)
