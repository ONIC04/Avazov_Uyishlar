#import math
#import requests
import random
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

# Rang almashtiruvchi dastur
# Oynaga bitta Label va bitta Button joylashtiring. Button bosilganda Labelning matn rangi tasodifiy rangga o'zgaradigan dastur yozing.
# Misol ranglar: qizil, ko'k, yashil, sariq.

colors = [
    "Red", "Blue", "Green", "Yellow", "Black", 
    "White", "Orange", "Purple", "Pink", "Brown", 
    "Gray", "Cyan", "Magenta", "Silver", "Gold", 
    "Maroon", "Navy", "Olive", "Teal", "Beige"
]

px = 38
app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("r: rang")
oyna.setGeometry(0, 0, px*9, px * 5)
oyna.setStyleSheet("background-color: #092e2c")

text = QLabel(oyna)
text.setText("Faundasion N204")
text.setGeometry(px*3, px, px * 3, px)
text.setStyleSheet("border: 2px solid black;") 

button = QPushButton(oyna)
button.setText("choice")
button.setGeometry(px * 3, px*3, px*3, px)
button.setStyleSheet("background-color: #642080")

def bos():
    rang = random.choice(colors)
    text.setStyleSheet(f"border: 2px solid black; color: {rang}")
button.clicked.connect(bos)



oyna.show()
app.exec_()