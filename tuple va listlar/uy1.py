import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')
#  a dan b sonigacha juft sonlarlarni to'g'ri tartibda listga joylashtirish. a va b input orqali olinsin.

a, b = map(int, input("Sonlarni kiriting: ").split())
list1 = []
sortlash1 = []
for i in range(a, b):
    if i % 2 == 0:
        list1.append(i)
    
print(f"{list1}")


