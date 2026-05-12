import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# Uchta set berilgan, birinchi va ikkinchi set uchun umumiy bo'lgan lekin uchinchi setda mavjud bo'lmagan elementlarni chiqaring.

set1={'olma', 'anor', 'youtube', 'instagram', 'gilos'}
set2={'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
set3={'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}

print(f"{(set1 & set2) - set3}")

