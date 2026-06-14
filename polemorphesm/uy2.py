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

# Harflar(ruscha, inglizcha) bilan ishlash uchun Convertor nomli class yarating.
# Bu classga ru_to_en (ruscha matnni harflarini inglizcha holatini qaytaradi) va en_to_ru (inglizcha matnni harflarini ruscha holatini qaytaradi) nomli metodlar yozing.
# Masalan, en_to_ru metodiga "Salom dunyo" kiritilsa "Ð¡Ð°Ð»Ð¾Ð¼ Ð´ÑƒÐ½Ñ‘" holatga o'tkazsin. Ð, Ñ, ÑŽ kabi harflarga etibor bering.

class Convertor:
        
    def en_to_ru(self, s,  h: dict):
        s1 = ""
        i = 0
        while i < len(s):
            if s[i: i+2] in h:
                s1 += h[s[i: i+2]]
                i += 2
            elif s[i] in h:
                s1 += h[s[i]]
                i += 1
            else:
                s1 += s[i]
                i += 1
                    
        print()
        print(s1)  
        print() 
    
    def ru_to_en(self, s, h: dict):
        h1 = {}
        for k, q in h.items():
            h1[q] = k
        s1 = ""
        i = 0
        while i < len(s):
            if s[i:i+2] in h1:
                s1 += h1[s[i: i+2]]
                i += 2
            elif s[i] in h1:
                s1 += h1[s[i]]
                i += 1
            else:
                s1 += s[i]
                i += 1
        
        print()
        print(s1)
        print()

    
c = Convertor()
harflar = {
    "SH": "Ш", "Sh": "Ш",
    "CH": "Ч", "Ch": "Ч",
    "YO": "Ё", "Yo": "Ё",
    "YU": "Ю", "Yu": "Ю",
    "YA": "Я", "Ya": "Я",
    "ZH": "Ж", "Zh": "Ж",
    "TS": "Ц", "Ts": "Ц",
    "NG": "НГ", "Ng": "Нг",
    "O'": "Ў", "G'": "Ғ",

    "sh": "ш", "ch": "ч",
    "yo": "ё", "yu": "ю", "ya": "я",
    "zh": "ж", "ts": "ц", "ng": "нг",
    "o'": "ў", "g'": "ғ",

    "A": "А", "B": "Б", "V": "В",
    "G": "Г", "D": "Д", "E": "Е",
    "F": "Ф", "H": "Ҳ", "I": "И",
    "J": "Й", "K": "К", "L": "Л",
    "M": "М", "N": "Н", "O": "О",
    "P": "П", "Q": "Қ", "R": "Р",
    "S": "С", "T": "Т", "U": "У",
    "X": "Х", "Y": "Й", "Z": "З",

    "a": "а", "b": "б", "v": "в",
    "g": "г", "d": "д", "e": "е",
    "f": "ф", "h": "ҳ", "i": "и",
    "j": "й", "k": "к", "l": "л",
    "m": "м", "n": "н", "o": "о",
    "p": "п", "q": "қ", "r": "р",
    "s": "с", "t": "т", "u": "у",
    "x": "х", "y": "й", "z": "з",
}

stopp = 0
st = None
while 1:
    try:
        print("1- RU -> EN\n2- EN -> RU")
        t = int(input(">>> "))
        if t == 2:
            s = input("String kiritng: ")
            c.en_to_ru(s, harflar)
        elif t == 1:
            s = input("String kiritng: ")
            c.ru_to_en(s, harflar)
        else:
            print("Xato qayta tanlov qiling!")
        stopp += 1
        if stopp >= 2:
            print("Anlayotni tugatasizmi (1- ha):(yoke istalgan narsa)")
            st = input(">>> ")
        if st == "1" or st == "ha":
            break
        
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        
