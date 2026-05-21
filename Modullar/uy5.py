import math
import random
import datetime
import os, sys
import time
import pytz
import json
from deep_translator import GoogleTranslator as tarjimon #uzimizni tranlator yaxshi ishlamadi bu yaxshi ekan aytishlaricha.. join so'zlarni split qilib srting qilib beradi😅
from collections import Counter, defaultdict
print('\033[2J\033[3J\033[H', end='')
#  Listda turli ma'lumotlar berilgan. Listdagi string turidagi ma'lumotlarni dict'ga inglizcha tarjimasi bilan yozing.

try:
    l1 = ["salom", "dastur", 2.5, "yordam", 34, "kitob"]
    l = []
    asl = []
    t = tarjimon(to_lang="en", from_lang="uz")
    for i in range(len(l1)):
        if isinstance(l1[i], str):
            asl.append(l1[i])
            l.append(t.translate(l1[i]))
    
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")
else:
    d = {}
    for i in range(len(asl)):
        d[asl[i]] = l[i]
        print(f"{asl[i]}: {l[i]}")
      
    print()
    print()
    print(f"{d}")
      
    
    
        
    
    