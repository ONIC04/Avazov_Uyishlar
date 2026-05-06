import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')
#   For orqali 1 dan n gacha sonlar orasida juftlarni kamayish tartibida chiqaring.

n = int(input("n = "))
for i in range(n+1, 0, -1):
    if i % 2 == 0:
        print(i, end=" ")
