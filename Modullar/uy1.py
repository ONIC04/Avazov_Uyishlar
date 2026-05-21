import math
import random
import datetime
import os, sys
import time
import json
import pytz
from collections import Counter, defaultdict
print('\033[2J\033[3J\033[H', end='')
#  datetime modulidan foydalanib, foydalanuvchiga hozirgi sanani chiqaruvchi dastur tuzing.
mintaqa = pytz.timezone("Asia/Tashkent")
data = datetime.datetime.now(mintaqa)

vaqt = data.strftime("%H : %M : %S")
sana = data.strftime("%d / %m / %y")
print(f"Sanaa: {sana} \n Vaqt: {vaqt}")