import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

#  Input orqali kiritilgan string ma'lumotlarni tuplega bittalab(har bir belgisini) joylashtiring.

matn = input("String: ")
list1 = []
for i in matn:
    list1.append(i)
t = tuple(list1)
print(f"{t}")
