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

# Phone(Telefon) nomli class yarating(brand, model, narx, yili kabi attributelar bilan).
# Bu classga narxni o'zgartirish uchun update_price nomli metod yozing.

class Phone:
    def __init__(self, b, m, n, y):
        self.brend = b
        self.model = m
        self.narx = n
        self.yili = y

class Narx(Phone):
    def __init__(self, b, m, n, y):
        super().__init__(b, m, n, y)
    
    def update_price(self, summa):
        n = 0
        while 1:
            try:
                if n >= 1:
                    summa = float(input("\nSummani kiriting: "))
                    print()
                print("\n1- Narxni oshirish\n2- Narxni kamaytirish")
                t = int(input(">>> "))
                print()
                if t == 1:
                    self.narx += summa
                    print(f"\nNarx oshirildi: Hozirgi narxi {self.narx}\n")
                    break
                elif t == 2:
                    if self.narx >= summa:
                        self.narx -= summa
                        print(f"\nNarx kamaytirildi: Hozirgi narxi -> {self.narx}\n")
                        break
                    else:
                        print("\nSumman narxdan baland qayta tanlov qiling!")
                        n += 1
                else:
                    print("\nXato tanlov qayta kiritng!\n")
            except Exception as e:
                print(f"\nXatolik yuz berdi: {e}\n")
                
n = Narx(input("Bred: "), input("Model: "), float(input("Narxi: ")), int(input("Yili: ")))
n.update_price(float(input("Summani kriting: ")))
                
            
                    
        