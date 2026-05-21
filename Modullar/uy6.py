import math
import random
import datetime
import os, sys
import time
import pytz
import json
# from deep_translator import GoogleTranslator as tarjimon
from collections import Counter, defaultdict
print('\033[2J\033[3J\033[H', end='')
# Filmlar va ularning bosh qahramonlari haqida dict berilgan. Foydalanuvchi film nomini kiritadi va shu film boshqa qahramonini chiqaring. 
# Agar film nomi xato kiritilsa "Bunday film yo'q" xabarini chiqaring. Dict'ning get metodidan foydalanish mumkin emas. try except bilan ishlang
try:
    filmlar = {
    "Titanic": "Jack Dawson",
    "Harry Potter": "Harry Potter",
    "The Dark Knight": "Bruce Wayne (Batman)",
    "The Matrix": "Neo (Thomas Anderson)",
    "Forrest Gump": "Forrest Gump",
    "Gladiator": "Maximus Decimus Meridius",
    "Inception": "Dom Cobb",
    "Spider-Man": "Peter Parker",
    "Iron Man": "Tony Stark",
    "The Lord of the Rings": "Frodo Baggins"
}
    s = input("Film nomini kiriting: ")
    # topildi = 0
    for k, q in filmlar.items():
        if k.lower() == s.lower():
            print(f"{k}: {q}")
            break   

except Exception as e:
    print(f"Bunday filim yo'q: {e}")
    
else:
    print("Bunday film topilmadi!!!")
    