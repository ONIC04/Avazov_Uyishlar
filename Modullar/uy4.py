import math
import random
import datetime
import os, sys
import time
import pytz
import json
from collections import Counter, defaultdict
print('\033[2J\033[3J\033[H', end='')
#  Quyidagi ikki 2x2 o'lchamdagi matritsani qo'shing va natijaviy matritsani chiqaring.

try:
    A = [
        [1, 2],
        [3, 4]
    ]

    B = [
        [5, 6],
        [7, 8]
    ]
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

else:
    l = []
    for i in range(len(A)):
        l1 = []
        for j in range(len(A[0])):
            l1.append(A[i][j] + B[i][j])
        l.append(l1)
    print("C = [")
    for i in l:
        for j in i:
            print(f"{j:4d}", end="")
        print()
    print("]")
            
    
            
         
    


