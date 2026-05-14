import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# Mashinalar va ularning nechta sotilgani haqida dictionary berilgan. Eng ko'p va eng kam sotilgan mashina turini chiqaring.
car_count = {
    "Chevrolet": 120,
    "Toyota": 95,
    "BMW": 60,
    "Kia": 75
}
kam = min(car_count.values())
kup = max(car_count.values())
print(f"Eng ko'p sotilgan: {kup} \n Eng kam sotilgan: {kam}")

