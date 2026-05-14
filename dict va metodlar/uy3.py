import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')
#   Mashinalarning tezligi haqidagi dictionary berilgan. Mashina nomi va tezligini tezlik bo'yicha kamayish tartibida(kattadan kichikka) chop eting.

speed = {
    "Tesla": 250,
    "BMW": 240,
    "Mercedes": 260,
    "Audi": 230
}
l = list(speed.items())

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i][1] < l[j][1]:
            l[i], l[j] = l[j], l[i]
    
for i in l:
    print(f"{i}")
    
    

