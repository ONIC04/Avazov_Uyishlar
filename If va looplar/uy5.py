import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')
#  Barcha ikkixonali sonlar orasida tub sonlarni chiqaruvchi dastur

for son in range(10, 99):
    tub = 1
    for i in range(2, son):
        if son % i == 0:
            tub = 0
            break
    if tub == 1:
        print(son, end=" ")