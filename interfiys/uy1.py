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
from PyQt5.QtCore import QTimer
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

# Tugmacha bosilganda Labelga 1 va 100 orasidagi random sonni chiqaruvchi dastur yozing.

taymer = QTimer()

px = 38
y = round(px * 2.3)

app = QApplication([])

oyna = QWidget()

oyna.setWindowTitle("1-100: r - 10")
oyna.setGeometry(0, 0, px * 5, px * 5)
oyna.setStyleSheet("""
                   background-color: #16e8f0;
                   """)

son = QLabel(oyna)
son.setGeometry(y, px, px, px)
son.setStyleSheet("""
                  color: red;
                  """)

button = QPushButton(oyna)
button.setText("r: Start")
button.setGeometry(px * 1, px * 3, px * 3, px)
button.setStyleSheet("""
                     background-color: #4bfa62;
                     border-radius: 16px;
                     color: red;
                     """)
ss = 0
def bos():
    global ss
    ss += 1
    r = random.randint(1, 100)
    son.setText(str(r))
    if not taymer.isActive():
        taymer.start(1000)
    button.setStyleSheet("""
                     background-color: green;
                     color: red;
                     border-radius: 16px;
                     """)
    if ss >= 10:
        oyna.close()
    
    QTimer.singleShot(150, lambda: button.setStyleSheet("background-color: #4bfa62; color: red; border-radius: 16px;"))
    
button.clicked.connect(bos)


oyna.show()
app.exec_()


