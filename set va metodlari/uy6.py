import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# Ikkita set berilgan, bu setlarning umumiy bo'lmagan elementlari yig'indisidan, umumiy elementlari yig'indisini ayiring.

set1={4,5,6,7,8,9}
set2={5,6,7,10,11}

l = list(set1 & set2)
l1 = list(set1 ^ set2)

y = 0
y1 = 0

for i in range(len(l)):
    y = y + l[i]
    
for i in range(len(l1)):
    y1 = y1 + l1[i]
    
print(f"Natija: {y1-y}")
