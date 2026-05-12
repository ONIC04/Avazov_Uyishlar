import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# Sonlardan iborat ikkita set berilgan. Shu setlarning umumiy bo'lmagan elementlarini kamayish tartibida chiqaring.

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

l = list(set1 ^ set2)
l.reverse()
print(f"{l}")


