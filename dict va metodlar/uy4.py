import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# Shaxslarning kasblari haqida dictionary berilgan. Bu dictionarydan foydalanib shaxsning ismi kiritilsa uning kasbini chiqaruvchi dastur kodini yozib bering.


professions = {
    "Bill Gates": "Dasturchi",
    "Cristiano Ronaldo": "Futbolchi",
    "Elon Musk": "Tadbirkor",
    "Messi": "Futbolchi"
}
ism = input("Shaxs ismini kiriting: ")
for i in professions:
    if i == ism:
        print(f"{ism}: {professions[i]}")
        
    
    


