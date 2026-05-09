import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# List ichida tuplelar berilgan va ushbu tuplelarning oxirgi elementini 100 bilan almashtiring.
list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

for i in range(len(list1)):
    l = list(list1[i])
    l[-1] = 100
    list1[i] = tuple(l)

print(f"{list1}")
