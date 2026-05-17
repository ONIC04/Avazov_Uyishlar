import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# Kiritilgan string ma'lumotini dictionaryga har bir belgi keyga va ushbu belgi nechtaligi valuega yozing. 


def qiymat(l: list, l1: list) -> list:
    for i in range(len(l)):
        l1.append(l.count(l[i]))


def dictt(l: list, l1: list) -> list:
    d = {}
    for i in range(len(l)):
        d[l[i]] = l1[i]
    
    return d


def print_dict(d: dict) -> dict:
    for i in d:
        print(f"{i} : {d[i]}")
   
   
def list_dict(d: dict) -> dict:
    ld = []
    for i in d:
        ld.append(i)
        ld.append(d[i])
    return ld     

s = input("Matn: ")
l = list(s)
l1 = []
qiymat(l, l1)
natija = dictt(l, l1)
d = print_dict(natija)
print("<- - ->"*10, "\n\n")
ld = list_dict(natija)
print(f"{ld}")
print("\n\n")
print(natija)
print("\n\n\n")


    


