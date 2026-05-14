import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

#  Cars nomli dictionary berilgan, bu dictionarydagi eng qimmat va eng arzon avtomobilni va avtomobillarning o'rtacha qiymatini chiqaring.

cars = {
    "Malibu": 35000,
    "Spark": 12000,
    "Cobalt": 18000,
    "Tracker": 28000
}
qimmat = max(cars.values())
arzon = min(cars.values())
u = 0
s = 0
for i in cars:
    u = u + cars[i]
    s += 1
    
    
print(f"Eng arzoni: {arzon} \n Eng qimatti{qimmat} \n O'rtachasi: {u/s:.1f}")
