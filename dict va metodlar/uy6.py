import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

# Quyida kitoblar haqida ma'lumot yozilgan dictionary berilgan.
# Sizning vazifangiz foydalanuvchi input orqali kitob nomini kiritadi, berilgan nomdagi kitob haqida ma'lumotlarni chop etish. 
# Agar kitob dict ichida yo'q bo'lsa "Kitob topilmadi" xabarini chiqarish. Kitob nomi katta harfda kiritilganda ham kichik harfda kiritilganda ham kitob topilsin.

books = {
    "O'tkan kunlar": {
        "muallifi": "Abdulla Qodiriy",
        "janri": "Roman",
        "chop etilgan yili": 1926,
        "tarjimalar soni": 5
    },
    "Mehrobdan chayon": {
        "muallifi": "Abdulla Qodiriy",
        "janri": "Roman",
        "chop etilgan yili": 1929,
        "tarjimalar soni": 3
    },
    "Kecha va kunduz": {
        "muallifi": "Cho'lpon",
        "janri": "Roman",
        "chop etilgan yili": 1934,
        "tarjimalar soni": 4
    },
    "Sarob": {
        "muallifi": "Abdulla Qahhor",
        "janri": "Roman",
        "chop etilgan yili": 1935,
        "tarjimalar soni": 2
    },
    "Ulug'bek xazinasi": {
        "muallifi": "Odil Yoqubov",
        "janri": "Tarixiy roman",
        "chop etilgan yili": 1974,
        "tarjimalar soni": 6
    },
    "Don Kixot": {
        "muallifi": "Migel de Servantes",
        "janri": "Roman",
        "chop etilgan yili": 1605,
        "tarjimalar soni": 50
    },
    "Urush va tinchlik": {
        "muallifi": "Lev Tolstoy",
        "janri": "Tarixiy roman",
        "chop etilgan yili": 1869,
        "tarjimalar soni": 45
    },
    "Alkimyogar": {
        "muallifi": "Paulo Koelyo",
        "janri": "Falsafiy roman",
        "chop etilgan yili": 1988,
        "tarjimalar soni": 80
    },
    "1984": {
        "muallifi": "Jorj Oruell",
        "janri": "Antiutopik roman",
        "chop etilgan yili": 1949,
        "tarjimalar soni": 65
    },
    "Kichkina shahzoda": {
        "muallifi": "Antuan de Sent-Ekzyuperi",
        "janri": "Falsafiy ertak",
        "chop etilgan yili": 1943,
        "tarjimalar soni": 300
    }
}
topildi = 0
nom = input("KItob nomini kiriting: ")
for i in books:
    if nom.lower() == i.lower():
        topildi = 1
        for k in books[i]:
            print(f"{k}: {books[i][k]}")

if topildi == 0:
    print("Bunday kitiob topilmadi!!!")

