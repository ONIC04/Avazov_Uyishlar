import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')
#  1 dan n gacha sonlarning juftlarini teskari tartibda chiqaring. n foydalanuvchi tomonidan kiritiladi.

n = int(input("n = "))

for i in range(n, 0, -1):
    if i % 2 == 0:
        print(i, end=", ")
        
