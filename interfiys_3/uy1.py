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
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QGridLayout)
#from PyQt5.QtCore import QTimer
#from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

# 1-masala. Telefon kitobi
# dict ko'rinishida: { "Ali": "99890...", "Vali": "99891..." }.
# PyQt5 oynasida QComboBox orqali ism tanlanadi, tanlangan odamning raqami yonida chiqadi.

class MainWindow(QWidget):
    def __init__(self, m):
        super().__init__()
        self.mijozlar = m
        l = ["Ism tanlang"]
        for i in self.mijozlar:
            l.append(i)
        self.setWindowTitle("Raqam izlash")
        self.grid = QGridLayout()
        self.ism = QComboBox()
        self.ism.addItems(l)
        self.grid.addWidget(self.ism, 1, 1)
        
        self.raqam = QLabel("Raqam")
        self.grid.addWidget(self.raqam, 1, 2)
        
        self.button = QPushButton("Aniqlash")
        self.button.setStyleSheet("background-color: green:")
        self.grid.addWidget(self.button, 2, 1, 1, 2)
        self.button.clicked.connect(self.aniqla)
        
        self.setLayout(self.grid)
        self.show()
        
    def aniqla(self):
        ism = self.ism.currentText()
        if ism == None or ism == "Ism tanlang":
            self.raqam.setText("Iltimos ism tanlang!")
        for i in self.mijozlar:
            if i.lower() == ism.lower():
                self.raqam.setText(self.mijozlar[i])
                break

mijozlar = {
    "Ali": "998901234567",
    "Vali": "998911234567",
    "Aziz": "998933456789",
    "Bekzod": "998945678901",
    "Davron": "998951122334",
    "Gulnora": "998971357924",
    "Dilnoza": "998981472583",
    "Sardor": "998991593746",
    "Madina": "998330246813",
    "Jasur": "998880135792",
}
app = QApplication([])
m = MainWindow(mijozlar)
app.exec_()

