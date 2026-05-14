import math
import random
import datetime
import os, sys
print('\033[2J\033[3J\033[H', end='')

#  Movies nomli dictionary berilgan. Bu dictionarydagi filmlardan faqat 2000-yildan keyin chiqarilganlarini nomini chop eting.

movies = {
    "Titanic": 1997,
    "Avatar": 2009,
    "Inception": 2010,
    "Interstellar": 2014
}
print("2000-yildan kiyin chiqagan filmlar!!!")
for i in movies:
    if movies[i] > 2000:
        print(f"{i}: {movies[i]}")
        






