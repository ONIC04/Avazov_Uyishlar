import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# Lambda funksiya orqali kiritilgan listdagi sonlarning kvadratga oshiruvchi funksiya yozing.


kv = lambda *x: x[0]**2


kvadrat = lambda x: x**2


l = [1,2,3,4,5,6,7,8,9,10]
i = 0
l1 = list(map(kvadrat, l))
print(l1)
print("<- - ->"*10)
print("yokeda")
l1 = []
for i in range(len(l)):
    l1.append(kv(l[i]))
    
print(f"{l1}")


