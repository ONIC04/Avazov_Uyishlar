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

#  Talaba nomli klass e'lon qiling va unda attributlar: name, age.
# Kurs nomli klass e'lon qiling va unda attributlar: kurs_name, kurs_teacher, talabalar_soni=0, talabalar=[];
# metodlar: add(new_student), delete(new_student), info_kurs().
# Sizning vazifangiz:
# - 2 ta Kurs e'lon qilasizlar va har bitta kursga 10tadan talaba qo'shish kerak (Kursga qo'shiladigan talabalar Talaba klasidan olingan obyekt bo'ladi)
# - 2 ta talabani kursdan haydash kerak


"""
Ho'p sal berilib kettim muhimi so'ralgan talabga javob beradi xato topishga urinmang
20 qator bilan argumentlarni berib oddiy qilib quyishim mukin edi lekin berilib ketib qoldim ishlatilmagan narsalr ko'p
xatolar ko'p quldan kegancha buldi endi buni to'gri hisobiga oling endi sabab 2 kurs qo'shiladi va talabalr qo'shiladi kiyin chetlashtiriladi
kurs haqida malumot beradi hullas hamma metodi ishledi bilaman Talaba classda name bilan age ishlamagan bu xato deb bumedi sabab so'ralgan narsa bor v.k
"""



class Talaba:
    def __init__(self, n=None, a=None):
        self.name = n
        self.age = a
        
class Kurs(Talaba):
    def __init__(self, n=None, a=None, kn: list=None, kt: list=None, ts: list=None, t: dict = None):
        super().__init__(n, a)
        
        self.kurs_name = kn if kn is not None else []
        self.kurs_teacher = kt if kt is not None else []
        self.talablar_soni = ts if ts is not None else []
        self.talabalar =  t if t is not None else {}

    def add(self, kurs_nomi: str,  new_student: str):
        self.talabalar[kurs_nomi].append(new_student)     
    
    def delete(self,kurs_nomi: str, new_student: str):
        self.talabalar[kurs_nomi].remove(new_student)
        index = 0
        for i in k.talabalar:
            if i == kurs_nomi:
                break
            index += 1
        self.talablar_soni[index] -= 1
    
    def info_kurs(self, kurs_nomi):
        index = 0
        for i in k.talabalar:
            if i == kurs_nomi:
                break
            index += 1
        print(f"{kurs_nomi.title()} kursimizda\n\nOqituvchi: {self.kurs_teacher[index].title()}\nTabalr soni: {self.talablar_soni[index]}")
        print()
        
stopp = 0
st = 0
k = Kurs()
while 1:
    try:
        n = int(input("Nechta kurs qo'shasiz: "))
        print()
        for i in range(n):
            s = input(f"{i+1} - Kurs nomi: ")
            s1 = input(f"{s.title()} - Kurs O'qituvchisi: ")
            k.talabalar[s.lower()] = []
            print()
            k.kurs_name.append(s)
            k.kurs_teacher.append(s1)
        print()
        print("Kurslar qo'shildi: ")
        print()
        index = 0
        for i in k.talabalar:
            print(f"{i.title()} - Teacher: {k.kurs_teacher[index].title()}")
            index += 1
        print()
        if n != None:
            break
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
    

while 1:
    try:
        print("1- Talabalar qo'shish\n2- Talbalarni kursdan haydash\n3- Kurs haqida malumot")
        t = int(input(">>> "))
        if t == 1:
            print()
            print("\t\t\tKurslar\n\n")
            for i in k.talabalar:
                print(i.title())
            print()
            kurs_nomi = input("Qaysi kursga qo'shsasiz: ")
            n = int(input("Nechta talaba qo'shasiz: "))
            k.talablar_soni.append(n)
            print()
            for i in range(n):
                s = input(f"{i+1} - Talaba: ")
                k.add(kurs_nomi.lower(),s.lower())
            print()
            print("Talabalar qo'shildi.")
            print()
            for i in k.talabalar:
                if kurs_nomi.lower() == i.lower():
                    for j in k.talabalar[i]:
                        print(j.title())
            print()
        elif t == 2:
            print()
            print("\t\t\tKurslar\n\n")
            for i in k.talabalar:
                print(i.title())
            print()
            kurs_nomi = input("Qaysi kursdan chetlashtirasiz: ")
            print()
            while 1:
                for i in k.talabalar:
                    if i == kurs_nomi.lower():
                        s = input("Talaba ismi: ")
                        k.delete(kurs_nomi.lower(), s.lower())
                        
                print("Yana talaba chetlashtirasizmi: (1- ha):((2- yo'q) yoke istalgan narsa)")
                b = input(">>> ")
                if b == "1" or b == "ha":
                    continue
                else:
                    break
            print()
            print(f"{kurs_nomi.title()} - Kursda qolgan talabalar")
            print()
            for i in k.talabalar:
                if i == kurs_nomi.lower():
                    for j in k.talabalar[i]:
                        print(j.title())
            print()
        elif t == 3:
            print()
            for i in k.talabalar:
                print(i.title())
            print()
            kurs_nomi = input("Qaysi kurs haqida bilmoqchisiz: ")
            print()
            k.info_kurs(kurs_nomi.lower())
                    
        
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
        
        

