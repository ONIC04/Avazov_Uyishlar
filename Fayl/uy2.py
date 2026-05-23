import math
import random
import datetime
import os, sys
import time
import pytz
from colorama import Fore, Style

import json
import wikipediaapi as wk
from collections import Counter, defaultdict
#  Foydalanuvchi so'z kiritadi, bu kiritilgan so'z fayl ichida bor yoki yo'qligini chiqaring. (Istalgan faylga ixtiyoriy matn yozishingiz mumkin.)
print('\033[2J\033[3J\033[H', end='')

wiki = wk.Wikipedia(user_agent="Avazov", language="uz")

try:
    izlash = input("Qidirmoqchi bo'lgan malumotingizni kiriting: ")
    malumot = wiki.page(izlash).summary
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

else:
    qizil = Fore.RED 
    yashil = Fore.GREEN
    reset = Fore.RESET
    with open("Avazov_Uyishlar/Fayl/2-uy.json", "w+") as file:
        json.dump(malumot.split(". "), file, ensure_ascii=False, indent=4)
        file.seek(0)
        l = " ".join(json.load(file)).split()
        qidir = input("Malumot ichidan qanday so'z izlayabsiz Dilrabo opa😅: ")
        topildi = 0
        for i in l:
            if i.lower() == qidir.lower():
                topildi = 1
                print(yashil + f"Siz izlagan so'z malumot ichidan topildi: {qidir}" + reset)
                break
        if topildi == 0:
            print(qizil + "Siz izlagan so'z topilmadi!!!" + reset)