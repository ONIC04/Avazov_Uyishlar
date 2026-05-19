import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')
# Berilgan dictionaryni qiymatlariga ko'ra tartiblab kalitlarini chiqaring.

def tartib(my_dict: dict):
    natija = sorted(my_dict, key=my_dict.get)
    return natija
    
my_dict = {
    "t": 3,
    "p": 1,
    "y": 2,
    "o": 5,
    "h": 4,
    "n": 6,
}    
javob = tartib(my_dict)
for i in javob:
    print(f"{i}")
    

    
    
