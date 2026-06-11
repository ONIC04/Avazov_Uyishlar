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

# Restoran nomli class yarating(Ish vaqti, menyusi kabi attributelar bilan).
# Bu classga menyuga yangi ovqat qo'shish uchun add_food nomli metod yozing. Ish vaqtini qaytaruvchi get_work_time metodini yozing.

class Restoran:
    def __init__(self, n, ishv, menyu: list = []):
        self.nomi = n
        self.ish_vaqti = ishv
        self.menyu = menyu

class Nom(Restoran):
    def __init__(self, n, ishv, menyu = []):
        super().__init__(n, ishv, menyu)
        
    def add_food(self, s: str):
        self.menyu.append(s)
    
    def get_work_time(self):
        return self.ish_vaqti
    
m = ["Sho'rva", "Mastava", "Norin", "Choy"] 
nn = Nom("Milliy taomlar","09:00 - 21:00", m)
nn.add_food("Shashlik")
print(f"{nn.nomi} <- - -> Ish vaqti: {nn.get_work_time()}")
print()
print("\t\t Menyu \n")
for i in range(len(nn.menyu)):
    print(nn.menyu[i])
print()