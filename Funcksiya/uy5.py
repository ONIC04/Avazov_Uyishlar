import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')
# Listni Nta sonlar bilan input orqali kiriting. Ushbu sonlardan faqat 1marta takrorlanganlarni o'chiring.

def dublikatsz(n: int, l: list) -> int:
    """
    Shu joyga kelib esimga tushdi shu narsa: Funksiya listdagi dublikatlarni o'chiradi!
    """
    for i in range(n):
        s = int(input(f"{i+1} - son: "))
        l.append(s)
    for i in range(n-1,-1,-1):
        if l.count(l[i]) > 1:
            l.remove(l[i])
        


n = int(input("Massiv uzunligi: "))
l = []
dublikatsz(n, l)
print(f"{l}")

