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
from PyQt5.QtCore import QTimer
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

# Oynaga bir Label va ikkita Button joylashtiring: "+1" va "-1". Label dastlab 0 bo'ladi.
# +1 bosilganda qiymat oshadi, -1 bosilganda kamayadi.

px = 38
t_x = round(px* 3.7)
app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Hisoblagich")
oyna.setGeometry(0, 0, px*8, px*6)
oyna.setStyleSheet("background-color: #696b64;")

t = QLabel(oyna)
t.setText("0")
t.setGeometry(t_x, px, px, px)
t.setStyleSheet("font-size: 30px; color: red;")

button = QPushButton(oyna)
button.setText("+1")
button.setGeometry(round(px*2.5), px * 3, px *3, px)
button.setStyleSheet("background-color: #341469; color: green")

button1= QPushButton(oyna)
button1.setText("-1")
button1.setGeometry(round(px*2.5), round(px*4.2), px *3, px)
button1.setStyleSheet("background-color: #341469; color: red")

def bos():
    son = int(t.text()) + 1
    t.setText(str(son))
    button.setStyleSheet("background-color: #150b24; color: #160c26")
    QTimer.singleShot(150, lambda: button.setStyleSheet("background-color: #341469; color: green"))

button.clicked.connect(bos)

def bos1(son1):
    son = int(t.text()) - 1
    t.setText(str(son))
    button1.setStyleSheet("background-color: #150b24; color: #160c26")
    QTimer.singleShot(150, lambda: button1.setStyleSheet("background-color: #341469; color: red"))

button1.clicked.connect(bos1)

oyna.show()
app.exec_()
