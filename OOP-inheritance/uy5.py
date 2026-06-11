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

# Employee(Hodim) nomli class yarating(ismi, familiyasi, ishga joylashgan sanasi, lavozimi, maoshi, bonusi kabi attributelar bilan).
# Maoshi 10_000_000 dan kam bo'lgan hodimlarga 25% bonus beruvchi set_bonus nomli metod yozing.
# Yani oylik= 8_000_000, bonus=2_000_000 kabi

class Employees:
    def __init__(self, i, f, sana, l, m, b):
        self.ism = i 
        self.familya = f 
        self.sana = sana
        self.lavozimi = l
        self.maoshi = m
        self.bonusi = b
        
class Empaloyee(Employees):
    def __init__(self, i, f, sana, l, m, b):
        super().__init__(i, f, sana, l, m, b)
        
    def set_bonus(self, l):
        for i in l:
            if i.maoshi < 10_000_000:
                i.bonusi = i.maoshi * 0.25
                print(f"{i.ism} {i.familya} - ga 25 % bonus berildi: bonus {i.bonusi}")
        
            
    
    
e = Empaloyee("Laziz", "Abdullayev", "10- mart", "Yordamchi", 10_000_000, 0)
e1 = Empaloyee("Ali", "Valiyev", "3- dekabr", "Bug'altir", 9_000_000, 0)
e2 = Empaloyee("Kamron", "Karimov", "17- may", "Oddiy ishchi", 5_000_000, 0)
l = [e, e1, e2]
e.set_bonus(l)



    
    

