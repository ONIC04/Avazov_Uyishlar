import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')
#  Matn berilgan. Eng ko'p uchraydigan 3 ta so'zni toping. ( So'zlar faqat harflardan iborat bo'ladi.)
def aniqlash(s: str):
    l = []
    for i in s.split():
        l.append(i)
    d = {}  
    for i in l:
        d[i] = l.count(i)
    l1 = sorted(d, key=d.get, reverse=True)[:3]
    return l1

s = "olma nok olma gilos olma nok shaftoli"
print(aniqlash(s))

    

    

