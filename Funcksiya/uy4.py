import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

#  Ikkita butun sonlardan iborat listlar berilgan. 
# Ushbu ikkita listlarda ikkalasida ham uchraydigan sonlarni new nomli listga joylashtiring.

def ikkalasida(a: list, b: list, new: set ) -> int:

    new = set(a) & set(b)
    new = list(new)
    return new
    
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new = set()
new = ikkalasida(a,b, new)
print(new)