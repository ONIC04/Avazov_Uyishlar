import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')
#  Istalgan xonali sonning raqamlarini teskari tartibda chiqarib beruvchi dastur tuzing

n = int(input("n = "))
y = 0
while n > 0:
    q = n % 10
    y = y*10 + q
    n = n // 10
s = str(y)
for i in s:
    print(i, end=" ")
