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

# String nomli class yarating va unga to_lower, to_upper, is_lower, is_upper nomli metodlar yozing. 
# Tayyor string metodlaridan foydalanish mumkin emas!

class String:
    def __init__(self, h):
        self.harf = h
    
    def is_upper(self):
        if 65 <= ord(self.harf) <= 90:
            return True
        else: 
            return False
    
    def is_lower(self):
        if 97 <= ord(self.harf) <= 122:
            return True
        else:
            return False
    
    def to_upper(self):
        if 97 <= ord(self.harf) <= 122:
            return chr(ord(self.harf) - 32)
        else:
            return self.harf
            
    
    def to_lower(self):
        if 65 <= ord(self.harf) <= 90:
            return chr(ord(self.harf) + 32)
        else:
            return self.harf
        
stopp = 0
st = None
while 1:
    stopp += 1
    try:
        print("\t\t\tHarflar bilan ishlash\n\n")
        print("1- Harf kattami\n2- Harf kichikmi\n3- Harflarni katta harfga alishtirish\n4- Harflarni kichik harfga alishtirish")
        t = int(input(">>> "))
        if t == 1:
            print('\033[2J\033[3J\033[H', end='')
            ss = input("Harf kiriting: ")
            s = String(ss)
            print() 
            print(s.is_upper())
            print()
        elif t == 2:
            print('\033[2J\033[3J\033[H', end='')
            ss = input("Harf kiritng: ")
            s = String(ss)
            print()
            print(s.is_lower())
            print()
        elif t == 3:
            print('\033[2J\033[3J\033[H', end='')
            ss = input("Harf kiritng: ")
            s = String(ss)
            print()
            print(s.to_upper())
            print()
        elif t == 4:
            print('\033[2J\033[3J\033[H', end='')
            ss = input("Harf kiritng: ")
            s = String(ss)
            print()
            print(s.to_lower())
            print()
        else:
            print("Xato tanlov qayta kiritng!")
        if stopp >= 4:
            print("Anlayotni tugatasizmi (1- ha):(yoke istalgan narsa)")
            st = input(">>> ")
        if st == "1" or st == "ha":
            break
                
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        