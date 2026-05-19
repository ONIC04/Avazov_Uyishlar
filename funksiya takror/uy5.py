import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')
# So'zlardan iborat listda takrorlangan so'zlar va bo'sh so'zlarni olib tashlang.

def tozalash_ishlari(mylist: list):
    l = []
    for i in mylist:
        if i not in l and i != "":
            l.append(i)
    return l
    

    
mylist = ["olma", "", "olma", "gilos", ""]
javob = tozalash_ishlari(mylist)
print(f"{javob}")
