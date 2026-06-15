#import math
#import requests
#import random
#import datetime
#import os, sys
#import time
#import pytz
#import json
#from abc import ABC, abstractmethod
# from deep_translator import GoogleTranslator as tarjimon
#from collections import Counter, defaultdict
print('\033[2J\033[3J\033[H', end='')

class Student:
    def __init__(self, n: str, id: str):
        self.name = n
        self.student_id = id
        self.__grades = []
        
    def add_grade(self, grade: int) -> None:
        if 1 <= grade <= 100:
            self.__grades.append(grade)
            print(f"{grade} Baho qo'shildi!")
            
        else:
            print("Baho Xato")
    
    def calculate_average(self) -> float:
        if not self.__grades:
            return 0.0
        else:
            return sum(self.__grades)/len(self.__grades)
        
    
    def get_status(self, javob) -> str:
        if 90 <= javob <= 100:
            return "A'lo"
        elif 80 <= javob <= 89:
            return "Yaxshi"
        elif 70 <= javob <= 79:
            return "Qoniqarli"
        elif 1 <= javob <= 69:
            return "Qoniqarsiz"
        elif javob <= 0: 
            return "Xaydalasiz"
        else:
            return "100 oshdi Faxri yorliq olasiz😅"
    
s = Student(input("Ism: "), input("ID: "))
print()
n = int(input("Bahoni kiritng: "))
n1 = int(input("Bahoni kiriting: "))
print("\n\n")

s.add_grade(n)
s.add_grade(n1)
javob = s.calculate_average()
print("O'rtacha baho:", javob)

javob1 = s.get_status(javob)
print("Status:", javob1)

        
        

    
    
    
    
    
    
