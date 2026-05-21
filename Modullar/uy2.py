import math
import random
import datetime
import os, sys
import time
import json
from collections import Counter, defaultdict
print('\033[2J\033[3J\033[H', end='')
# Foydalanuvchi tug'ilgan sanani kiritsin (masalan: 1993-05-15). Siz esa bugungi kundan hisoblab nechta kun o'tganini hisoblang.
data = datetime.datetime.now()
try:
    kun1 = int(input("Tug;ulgan kuningizni kiriting: "))
    oy1 = int(input("Tug'ulgan oyinggizni kiriting:  "))
    yil1 = int(input("Tug'ulgan yilingizni kiriting: "))
    tugulgan = datetime.datetime(yil1, oy1, kun1)
    
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

else:
    farq = data - tugulgan
    print(f"Tug'ulganingizga {farq.days} kun bo'ldi")
    
    



