#import math
#import requests
#import random
#import datetime
#import os, sys
import time
#import pytz
#import json
# from deep_translator import GoogleTranslator as tarjimon
#from collections import Counter, defaultdict
print('\033[2J\033[3J\033[H', end='')

# Taqvim nomli class yarating 
# va unga hijriyga (Biz foydalanadigan grigoriyan taqvimida berilgan yilni hijriy yilga o'tkazadi)
# va grigoriyanga (hijriy yilni grigoriyan taqvimidagi yilga o'tkazadi),
# kabisami (berilgan yil kabisa yili yoki emasligini tekshiradi) metodlarini yozing. (grigoriy_yil - 622) * (365.25 / 354.367)

class Taqvim:
    def __init__(self, y):
        self.yil = y
        
    def grigoriyan(self):
        jy = int((time.localtime().tm_year - 622) * (365.25 / 354.367))
        kabisa = ""
        if 1 <= self.yil <= jy:
            g = round((self.yil * 354.367 / 365.25) + 622)
            if (g % 4 == 0 and g % 100 != 0) or g % 400 == 0:
                kabisa = "Ha"
            else:
                kabisa = "yo'q"
            return g, kabisa
        else:
            print(f"Hijriy yil 1 - dan {jy} - yil oralig'ida! qayta kiriting")
    
    def hijriy(self):
        kabisa = ""
        if 622 <= self.yil <= time.localtime().tm_year:
            h = round((self.yil - 622) * (365.25 / 354.367))
            if (self.yil % 4 == 0 and self.yil % 100 != 0) or self.yil % 400 == 0:
                kabisa = "ha"
            else:
                kabisa = "yo'q"
            return h, kabisa
        else:
            print("Grigoriyan 622 - yildan boshlanga qayta kiriting!")
    
stopp = 0
st = None
while 1:
    try:
        stopp += 1
        print("1- Yilni hijriyga o'tkazish\n2- Yilni grigoriyan ga o'tkazish")
        t = int(input(">>> "))
        if t == 2:
            yil = int(input("Yilni kiriting: "))
            t = Taqvim(yil)
            print()
            javob = t.grigoriyan()
            if javob:
                print("Grigoriyanga o'tkazildi:",javob[0], "Kabisya yilimi:" ,javob[1])
            print()
        elif t == 1:
            yil = int(input("Yilni kiritng: "))
            t = Taqvim(yil)
            print()
            javob = t.hijriy()
            if javob:
                print("Hijriyga o'tkazildi:", javob[0], "Kabisiya yilimi:", javob[1])
            print()
        else:
            print("Xato tanlov qayta kiriting!")
        if stopp >= 2:
            print("Amaliyotni tugatasizmi (1- ha):(yo'q yoke istalgan narsa)")
            st = input(">>> ")
        if st == "1" or st == "ha":
            break
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        