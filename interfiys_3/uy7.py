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
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QCheckBox, QRadioButton, QMessageBox, QVBoxLayout, QHBoxLayout, QGridLayout, QTextEdit)
#from PyQt5.QtCore import QTimer
#from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

# 7-masala. Kutubxona katalogi
# Kutubxona kitoblari listda saqlangan:
# ["Python Asoslari", "Flask Dasturlash", "Sun'iy Intellekt"]
# Qidiruv oynasiga matn yozilsa, mos kelgan kitoblar ro'yxatda chiqadi. Masalan: "Py" yozsa -> "Python Asoslari" chiqadi.

class MainWin(QWidget):
    def __init__(self, l : list):
        super().__init__()
        self.list = l
        self.setWindowTitle("Kutubxona")
        self.grid = QGridLayout()
        
        self.m = QLabel("Najija shu yerda chiqadi!")
        self.grid.addWidget(self.m, 1, 1, 1, 2)
        
        self.button = QPushButton("Izlash")
        self.grid.addWidget(self.button, 2, 1, 1, 2)
        self.button.clicked.connect(self.izla)
        
        self.line = QLineEdit()
        self.line.setPlaceholderText("Subtetr yoke so'z kiriitng...")
        self.grid.addWidget(self.line, 4, 1, 1, 2)
        
        self.setLayout(self.grid)
        self.show()
    
    def izla(self):
        string = self.line.text()
        n = len(string)
        t = 0
        for i in self.list:
            if i[:n].lower() == string.lower():
                self.m.setText(f"Topildi!: {i}")
                t = 1
                break
        if t == 0:
            self.m.setText("Topilma!")
        
l = [
    "Python Asoslari",
    "Flask Dasturlash",
    "Sun'iy Intellekt",
    "Django Web Kursi",
    "Ma'lumotlar Strukturasi va Algoritmlar",
    "PostgreSQL va Ma'lumotlar Bazasi",
    "Telegram Bot Yaratish",
    "Mashinali O'rganish (Machine Learning)",
    "Frontend Asoslari (HTML, CSS, JS)",
    "Kiberxavfsizlik va Tarmoqlar"
]      
app = QApplication([])
m = MainWin(l)
app.exec_()

