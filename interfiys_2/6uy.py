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
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QGridLayout)
#from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

stil_oyna = "background-color: #0b2e3b; color: #14991f"
stil_rang = "font-size: 20px; color: red;"
app = QApplication([])
class Orqaoladisanash(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Sanash luboychasiga😂")
        self.setStyleSheet(stil_oyna)
        self.grid = QGridLayout()
        
        self.text = QLabel("0")
        self.text.setStyleSheet(stil_rang)
        self.text.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.text, 1, 1, 1, 2)
        
        self.button = QPushButton("+1")
        self.button.setStyleSheet("color: green")
        self.grid.addWidget(self.button, 2, 1, 1, 2)
        self.button.clicked.connect(self.oshir)
        
        self.button1 = QPushButton("-1")
        self.button1.setStyleSheet("color: red")
        self.grid.addWidget(self.button1, 3, 1, 1, 2)
        self.button1.clicked.connect(self.kamay)
        
        self.setLayout(self.grid)
        self.show()
    def oshir(self):
        son = int(self.text.text()) + 1
        if son >= 0:
            self.text.setStyleSheet("color: green")
            self.text.setText(str(son))
        else:
            self.text.setText(str(son))
        
    def kamay(self):
        son = int(self.text.text()) - 1
        if son < 0:
            self.text.setStyleSheet("color: red")
            self.text.setText(str(son))
        else:
            self.text.setText(str(son))
        
        
o = Orqaoladisanash()
app.exec_()
        
        
