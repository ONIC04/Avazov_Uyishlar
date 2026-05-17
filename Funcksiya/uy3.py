import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

#  Har xil uzunlikdagi Listlar berilgan va sizning vazifangiz ushbu listlarni quyidagi shartlar asosida yangi listga birlashtirish.
#  Yangi listga birinchi list1 elementi va keyin list2 elementini ketma-ketlikda joylashtiring.
def birlashtirish(list1: list, list2: list, list3: list) -> int:
    for i in range(min(len(list1), len(list2))):
        list3.append(list1[i])
        list3.append(list2[i])
    
    
list1 = list(map(int, input("Massiv: ").split()))
list2 = list(map(int, input("Massiv: ").split())) ## ming bor uzur majbur buldim split ishlatishga bu dinamik xotira bilan ishlagani uchun masalada berilgan 2 ta inputni birdan kiritomadim birxil natija xaytarib quyayabdi qo'lda kiritishizga to'gri keladi edi sorry

list3 = []

birlashtirish(list1,list2,list3)
print(f"{list3}")

