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
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QGridLayout)
#from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

stil_oyna = "background-color: #0b2e3b; color: #14991f"
stil_rang = "font-size: 30px; color: red;"
parol = "1234"
app = QApplication([])
class Tekshiruv(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tekshuruv")
        self.setStyleSheet(stil_oyna)
        self.grid = QGridLayout()
        
        self.line = QLineEdit()
        self.line.setPlaceholderText("Parolni kiritting...")
        self.grid.addWidget(self.line, 1, 1, 1, 2)
        
        self.text = QLabel("")
        self.text.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.text, 2, 1, 1, 2)
        
        self.button = QPushButton("Kirish")
        self.button.setStyleSheet(stil_rang)
        self.grid.addWidget(self.button, 3, 1, 1, 2)
        self.button.clicked.connect(self.tekshir)
        
        
        self.setLayout(self.grid)
        self.show()
        
    def tekshir(self):
        kiritilgan_parol = self.line.text()
        if kiritilgan_parol == parol:
            self.text.setText("To'gri✅")
            self.text.setStyleSheet("color: green")
        elif kiritilgan_parol == None or kiritilgan_parol == "" or kiritilgan_parol == " " or kiritilgan_parol == "\n":
            self.text.setText("Iltmos parolni kiriting...")
            self.text.setStyleSheet("color: #13ede6")
        else:
            self.text.setText("Noto'g'ri❌")
            self.text.setStyleSheet("color: red")


t = Tekshiruv()
app.exec_()