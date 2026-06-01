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
# Bank hisob kalkulyatori.
# Depozit summasi, foiz stavkasi va yil sonini argument sifatida oladigan funksiya yozing va yakuniy summani qaytaring.
# Parametr: depozit=10000, foiz=24, yil=3
# Return: 17200


def hisob(depozit: int, foiz: int, yil: int) -> int:
    foizz = depozit * (foiz/100)
    yill = foizz * yil
    jami = depozit + yill
    return int(jami)

try:
    depozit = int(input("Depozit: "))
    foiz = int(input("Foiz: "))
    yil = int(input("Necha yilga: "))
    javob = hisob(depozit, foiz, yil)
    print(f"{yil} - Yilga <- - -> {foiz} Foizda {javob} So'm olasiz")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")
    