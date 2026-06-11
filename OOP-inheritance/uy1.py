#import math
#import requests
#import random
#import datetime
#import os, sys
#import time
#import pytz
#import json
# from deep_translator import GoogleTranslator as tarjimon
#from collections import Counter, defaultdict
print('\033[2J\033[3J\033[H', end='')

# Avto nomli class yarating(nomi, rangi, narxi, probegi, tezligi kabi attributelar bilan).
# Bu classga probegni o'zgartirish uchun update_probeg va narxni o'zgartirish uchun update_narx nomli metodlar qo'shing.

class Avto:
    def __init__(self, n, r, narx, p, t):
        self.nomi = n
        self.rang = r
        self.narx = narx
        self.probeg = p
        self.tezlik = t
    
    def update_probeg(self, p):
        if self.probeg >= p:
            self.probeg -= p
            print()
            print(f"Probeg ortga qaytarildi: hozirgi probeg - {self.probeg}")
            print()
        else:
            print("Probeg yurilgan probekdan katta bulmasligi kerak! - Qayta Tanlang")
    
    def update_narx(self, n, tt):
        if tt == 1:
            self.narx += n
            print()
            print(f"Narx oshirildi: hozirgi narx - {self.narx}")
            print()
        if tt == 2:
            if self.narx >= n:
                self.narx -= n
                print()
                print(f"Narx kamaytirildi: hozirgi narx - {self.narx}")
                print()
            else:
                print("Narxni o'rnatilgan narxdan ko'p qiymatga o'zgartirolmaysiz! - Qayta Tanlang")
    
stopp = 0 
st = 0
       
a = Avto(input("Mashina nomi: "), input("Rangi: "), float(input("Narxi: ")), float(input("Probegi: ")), int(input("Tezligi: ")))  
while 1:
    try:
        print("1- probeg ortga qaytarish\n2- Narxni o'zgartirish")
        t = int(input(">>> "))
        if t == 1:
            print()
            a.update_probeg(int(input("Qancha ortga qaytarmoqchisiz: ")))
        elif t == 2:
            while 1:
                try:
                    print("1- Narxni oshirish\n2- Narxni kamaytirish")
                    tt = int(input(">>> "))
                    if tt == 1: 
                        print()
                        a.update_narx(float(input("Qanchaga oshirasiz: ")), tt)
                        break
                    elif tt == 2: 
                        print()
                        a.update_narx(float(input("Qanchaga kamaytirasiz: ")), tt)
                        break
                    else:
                        print("Noto'gri tanlov qayta kiriting!")
                        print()
                except Exception as e:
                    print(f"Xatolik yuz berdi: {e}")
        else:
            print("Noto'gri tanlov qayta kiriting!")   
        if stopp >= 1:
            while 1:
                print("Amalyotni tugatasizmi- (1 - ha):(2 - yo'q)")  
                ttt = input("Amalyot >>>  ")
                if ttt == "1" or ttt == "ha":
                    st = 1
                    break
                elif ttt == "2" or ttt == "yo'q":
                    st = 0
                    break
                else:
                    print("Xato tanlov qayta kiritng")
        if st == 1:
            break
        stopp += 1          
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        