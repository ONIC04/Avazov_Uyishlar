import math
import random
import datetime
import os, sys
import time
import pytz
import json
from collections import Counter, defaultdict
print('\033[2J\033[3J\033[H', end='')
# Kelgusi Mustaqillik bayramigacha (YYYY-09-01) necha kun qoldiganini hisoblovchi dastur tuzing.
data = datetime.datetime.now()

try:
    yil = int(input("Shu yil: "))
    oy = int(input("Hozirgi oy: "))
    kun = int(input("Bugungi kun: "))
    bugunsana = datetime.datetime(yil, oy, kun)
    bayram = datetime.datetime(yil, 9, 1)
    
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")
    
else: 
    if bugunsana > bayram:
        bayram = datetime.datetime(yil+1, 9, 1)
        
    qolgankun = bayram - bugunsana
    print(f"Mustaqillik bayramiga: {qolgankun.days} kun qolgi")
    