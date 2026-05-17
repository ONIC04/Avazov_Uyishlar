import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# Listlar ro'yxatidan dublikatlarni olib tashlang.

def olibtashlash(l, l1: list) -> int:
    for i in l:
        if i not in l1:
            l1.append(i)
        
 
 
            
l = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
l1 = []
olibtashlash(l,l1)
print(f"{l1}")
