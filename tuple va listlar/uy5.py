import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# Sonlardan iborat listlarni o'zida saqlaydigan list berilgan. Ichki listlarning elementlar yig'indisi eng katta bo'lgan listni toping.

l =  [ [1,2,3], [4,5,6], [10,11,12], [7,8,9] ]

j = 0
y1 = []
y2 = 0
index = 0

for i in range(len(l)):
    y = 0
    for j in range(len(l[i])):
        y = y + l[i][j]
    y1.append(y)
    if y > y2:
        y2 = y
        index = i
    

print(f"{max(y1)} - {l[index]}") # C bup ketti😅
