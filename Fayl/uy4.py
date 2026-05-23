import math
import random
import datetime
import os, sys
import time
import pytz
import json
# from deep_translator import GoogleTranslator as tarjimon
from collections import Counter, defaultdict
print('\033[2J\033[3J\033[H', end='')
# Fayl ichida butun sonlar yozilgan. Shu sonlarning o'rtacha qiymatini chiqaring.

with open("Avazov_Uyishlar/Fayl/4-uy.json", "r") as file:
    l = json.load(file).split()
    y = 0
    s = 0
    for i in l:
        y = y + int(i)
        s += 1
    print(f"O'rtacha qiymati: {math.ceil(y/s)}")
    