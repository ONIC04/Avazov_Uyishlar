import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# Foydalanuvchi ikkita so'z kiritadi, kiritilgan so'zlar anagram ekanini tekshiring.
# Anagram so'z deganda bir so'zning harflari o'rnini almashtirib ikkinchi so'zni hosil mumkin bo'lishi.

s = input("Birinchi so'z: ")
s1 = input("Ikkinchi so'z: ")

set1 = set(s)
set2 = set(s1)

print(f"{set1.issubset(set2) and set2.issubset(set1)}")

