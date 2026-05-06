import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

#  Kiritilgan sonni raqamlarini to'g'ri tartibda chiqaring.
n = int(input("n = "))
s = str(n)
for i in s: # range faqat sonlar ketma ketligi uchun ekan stringga bu shart emas ekan yana list ham bularkan "matn" = [0,1,2,3] - index muommo yo'q;
    print(i, end=" ")