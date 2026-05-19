import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')
# Har bir o'quvchining fanlar bo'yicha baholari berilgan. Har bir o'quvchi uchun o'rtacha ballni hisoblang.

def aniqlash(students: dict):
    for k, q in students.items():
        b = list(q.values())
        ortacha = sum(b) / len(b)
        print(f"{k}: {ortacha}")

students = {
  "Ali": {"math": 90, "en": 80},
  "Vali": {"math": 70, "en": 85}
}
aniqlash(students)