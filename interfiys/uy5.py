#import math
#import requests
#import random
#import datetime
#import os, sys
#import time
#import pytz
#import json
#from abc import ABC, abstractmethod
# from deep_translator import GoogleTranslator as tarjimon
#from collections import Counter, defaultdict
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit)
#from PyQt5.QtCore import QTimer
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

# Parol tekshiruvchi kichik ilova
# Oynaga bir LineEdit (parol kiritish uchun), bir Button va bir Label joylashtiring. Button bosilganda agar LineEditga "12345" yozilgan bo'lsa:
# Label -> "Parol to'g'ri" matnini ko'rsatadi.
# Aks holda:
# Label -> "Noto'g'ri parol" matnini ko'rsatadi.
px = 38
app = QApplication([])
parol = "1234"
oyna = QWidget()
oyna.setWindowTitle("Avtorzatsiya😅")
oyna.setGeometry(0, 0, px * 10, px * 5)
oyna.setStyleSheet("background-color: #b4e30b;")

line = QLineEdit(oyna)
line.setPlaceholderText("Parol...")
line.setGeometry(px, px, px*8, px)
line.setStyleSheet("background-color: black;")

button = QPushButton(oyna)
button.setText("Kirish")
button.setGeometry(px*2, px * 4, px * 6, px)
button.setStyleSheet("background-color: #28b526;")

tasdiq = QLabel(oyna)
tasdiq.setGeometry(px * 4, px*2, px*5, px)

def bos():
    if str(line.text()) == parol:
        tasdiq.setStyleSheet("color: green")
        tasdiq.setText("To'gri✅")
    else:
        tasdiq.setStyleSheet("color: red")
        tasdiq.setText("Notog'ri❌")
    
button.clicked.connect(bos)

oyna.show()
app.exec_()
