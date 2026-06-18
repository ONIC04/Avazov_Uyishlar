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
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton)
from PyQt5.QtCore import QTimer
print('\033[2J\033[3J\033[H', end='')

# 1ta label va 3ta Button yarating va 1-buttonni bosganda Ismingiz,
# 2-buttonni bosganda Familiyangiz va 3-buttonni bosganda tug'ilgan sanangiz Labelda chiqarib beruvchi dastur yozing.

oyna_stil = "background-color: #31babd"
stil = "font-size: 15px; font-weight: bold; color: #012421"
px = 38

app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Malumot!")
oyna.setGeometry(0, 0, px*10, px*10)
oyna.setStyleSheet(oyna_stil)

natija = QLabel(oyna)
natija.setGeometry(px*2, px, px * 8, px)
natija.setStyleSheet(stil)

b = QPushButton(oyna)
b.setText("ISM")
b.setGeometry(px * 2, px * 4, px * 6, px * 1)
b.setStyleSheet("font-weight: bold; background-color: #d44a1c; color: black; border: 2px solid black")

def bos():
    natija.setText("Husan")
    b.setStyleSheet("font-weight: bold; background-color: green; color: black; border: 2px solid black")
    QTimer.singleShot(150, lambda: b.setStyleSheet("font-weight: bold; background-color: #d44a1c; color: black; border: 2px solid black"))

b.clicked.connect(bos)

b1 = QPushButton(oyna)
b1.setText("FAMILIYA")
b1.setGeometry(px * 2, px * 6, px * 6, px * 1)
b1.setStyleSheet("font-weight: bold; background-color: #d44a1c; color: black; border: 2px solid black")

def bos1():
    natija.setText("Avazov")
    b1.setStyleSheet("font-weight: bold; background-color: green; color: black; border: 2px solid black")
    QTimer.singleShot(150, lambda: b1.setStyleSheet("font-weight: bold; background-color: #d44a1c; color: black; border: 2px solid black"))

b1.clicked.connect(bos1)

b2 = QPushButton(oyna)
b2.setText("YIL 0000.00.00")
b2.setGeometry(px * 2, px * 8, px * 6, px * 1)
b2.setStyleSheet("font-weight: bold; background-color: #d44a1c; color: black; border: 2px solid black")

def bos2():
    natija.setText("2004.12.09")
    b2.setStyleSheet("font-weight: bold; background-color: green; color: black; border: 2px solid black")
    QTimer.singleShot(150, lambda: b2.setStyleSheet("font-weight: bold; background-color: #d44a1c; color: black; border: 2px solid black"))

b2.clicked.connect(bos2)

oyna.show()
app.exec_()

