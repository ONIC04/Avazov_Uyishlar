import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')
#  Ombor nomli list berilgan, listdagi jami mahsulotlar miqdorini va eng kam qolgan 3ta mahsulotni toping.

def omborrda(ombor: list):
    y = 0
    for i in ombor:
        y = y + i["miqdor"]
    
    natija = sorted(ombor, key=lambda i: i["miqdor"])[:3]
    print(f"Umumiy mahsulotlar miqdori: {y}\nEng kam: {', '.join([i['mahsulot'] for i in natija])}") # join listdagi elementlarni bitta stringa aylantiradikan 😅 tan olaman ko'chirdim buni joyini 
    y1 = 0
    for i in natija:
        y1 += i["miqdor"]
        
    print(f"yoke bu miqdor: {y - y1}")
    
            






ombor = [
    {"mahsulot": "olma", "miqdor": 5},
    {"mahsulot": "nok", "miqdor": 9},
    {"mahsulot": "shaftoli", "miqdor": 7},
    {"mahsulot": "anor", "miqdor": 4},
    {"mahsulot": "banan", "miqdor": 6},
    {"mahsulot": "uzum", "miqdor": 8},
    {"mahsulot": "gilos", "miqdor": 2},
    {"mahsulot": "tarvuz", "miqdor": 1},
    {"mahsulot": "qovun", "miqdor": 3},
    {"mahsulot": "limon", "miqdor": 5}
]
omborrda(ombor)








