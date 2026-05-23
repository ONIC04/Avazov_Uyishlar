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
# Berilgan fayldagi barcha so'zlarning birinchi harfini katta harfga o'tkazuvchi dastur tuzing.
with open("Avazov_Uyishlar/Fayl/3-uy.json", "r+") as file:
    l = json.load(file).title()       
    file.seek(0)
    json.dump(l, file)

    
        