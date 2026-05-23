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
# Fayl ichida belgilarning ASCII raqamlari probel bilan yozilgan. Bu raqamlar ortida qanday gap yozilganini yangi faylga yozing.
with open("Avazov_Uyishlar/Fayl/1-uy.json", "w+") as file:
    json.dump("80 121 116 104 111 110 32 97 106 111 121 105 98 32 100 97 115 116 117 114 108 97 115 104 32 116 105 108 105", file)
    file.seek(0) #kursor uchun funksiya ekan parametri 0 kursorni boshiga qaytararkan +10 bering bunga -10 emas 
    l = json.load(file).split()
    l1 = []
    for i in l:
        n = int(i)
        l1.append(chr(n))
    s = ""
    for i in l1:
        s += i
    
    print(f"{s}") # join ishlatmadim ai ham ishlatmadim so'ramadim ham;
with open("Avazov_Uyishlar/Fayl/1-uy1.json", "w+") as file2:
    json.dump(s, file2)