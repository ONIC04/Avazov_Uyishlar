import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# Sonlardan iborat list berilgan. Barcha nol (0) raqamlarini listning oxiriga o'tkazing.

def natija(l: list) -> int:
    for i in range(len(l)-1,-1,-1):
        if l[i] == 0:
            l.pop(i)
            l.append(0)



l = [3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1]
natija(l)
print(f"{l}")


