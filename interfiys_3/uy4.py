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
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox,QMessageBox, QGridLayout)
# from PyQt5.QtCore import QTimer
#from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

# Supermarket savatchasi
# dictda mahsulotlar va narxlari:
# { "Olma": 5000, "Banan": 7000, "Sut": 12000 }
# PyQt5 oynasida foydalanuvchi mahsulotni tanlaydi va miqdorini kiritadi.
# Natijada savatdagi umumiy summa ko'rsatiladi. Bonus sifatida - umumiy summa 100 mingdan oshsa "Chegirma qo'llandi" xabari chiqsin.

class MainWindow(QWidget):
    def __init__(self, m: dict, l: list, d: dict):
        super().__init__()
        self.savat = m
        self.l = l
        self.d = d
        self.setWindowTitle("Savat")
        self.grid = QGridLayout()
        
        self.cbox = QComboBox()
        self.cbox.addItems(self.l)
        self.grid.addWidget(self.cbox, 1, 1)
        
        self.line = QLineEdit()
        self.line.setPlaceholderText("Maxsulot soni...")
        self.grid.addWidget(self.line, 1, 2)
        
        self.button = QPushButton("Savatga+")
        self.grid.addWidget(self.button, 2, 1, 1, 2)
        self.button.clicked.connect(self.qushish)
        
        self.button1 = QPushButton("Hisobla")
        self.grid.addWidget(self.button1, 3, 1, 1, 2)
        self.button1.clicked.connect(self.hisoblash)
        
        self.natija = QLabel("Jami summa shu yerda chiqadi!")
        self.natija.setStyleSheet("color: red;")
        self.grid.addWidget(self.natija, 4, 1, 1, 2)
        
        self.setLayout(self.grid)
        self.show()
        
    def qushish(self):
        tavar = self.cbox.currentText()
        soni = self.line.text().strip()

        if tavar == "Maxsulotlar":
            QMessageBox.warning(self, "Xato", "Iltimos mahsulot tanlang!")
            return

        if not soni.isdigit() or int(soni) <= 0:
            QMessageBox.warning(self, "Xato", "Iltimos to'g'ri son kiriting!")
            return

        soni = int(soni)
        self.d[tavar] = self.d.get(tavar, 0) + soni 
        self.line.clear()
        
    def hisoblash(self):
        jami = 0
        for tavar, soni in self.d.items():
            narx = self.savat[tavar]
            jami += narx * soni

        if jami > 100000:
            self.natija.setText(f"Jami: {jami} so'm — Chegirma qo'llandi!")
            self.natija.setStyleSheet("color: green;")
        else:
            self.natija.setText(f"Jami: {jami} so'm")
            self.natija.setStyleSheet("color: blue;")
    
            

mahsulotlar = {
    "Olma": 5000,
    "Banan": 7000,
    "Sut": 12000,
    "Non": 3000,
    "Tuxum": 1500,
    "Guruch": 14000,
    "Yog'": 25000,
    "Qand": 9000,
    "Choy": 18000,
    "Pomidor": 6000,
}

l = ["Maxsulotlar"]

for i in mahsulotlar:
    l.append(i)
d = {}
app = QApplication([])
m = MainWindow(mahsulotlar, l, d)
app.exec_()
    
    
