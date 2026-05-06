import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')
#  1 dan n gacha sonlarni va ularning yig'indisini chiqaring. n foydalanuvchi tomonidan kiritiladi.
y = 0
n = int(input("n = "))
for i in range(1, n+1):
    y += i
print(f"Yig'gindi: {y}")

