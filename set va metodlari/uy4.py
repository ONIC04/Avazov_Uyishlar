import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# Ikki do'st alohida shaharlar ro'yxatini to'pladi: Ikkala do'st ham borgan shaharlarni va faqat ali borgan shaharlarni chiqaring.

ali = {"Toshkent", "Samarqand", "Buxoro", "Andijon"}
vali = {"Toshkent", "Farg'ona", "Buxoro", "Xiva"}

print(f"Ikkalasi ham borgan: {ali & vali}\nFaqat ali borgan: {ali - vali}")


