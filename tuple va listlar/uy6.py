import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# List va String ma'lumotlarini berilgan. Listdagi barcha elementlarning boshiga berilgan stringni qo'shib qo'ying.

l = [1,2,3,4]
l2 = []
s = "emp"
for i in range(len(l)):
    l2.append(s + str(l[i]))
    
print(f"{l2}")
