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
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QCheckBox, QRadioButton, QMessageBox, QVBoxLayout, QHBoxLayout, QGridLayout, QTextEdit)
#from PyQt5.QtCore import QTimer
#from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

# 6-masala. To'plamdan tasodifiy tanlash
# listda talabalar ismlari saqlansin.
# Foydalanuvchi 'Tanlash' tugmasini bossa, dastur random.choice() yordamida bitta ismni chiqaradi.

class MainWin(QWidget):
    def __init__(self, l: list):
        super().__init__()
        self.list = l
        self.setWindowTitle("Random talaba")
        self.grid = QGridLayout()
        
        self.text = QLabel("Talaba ismi")
        self.grid.addWidget(self.text, 1, 1, 1, 2)
        
        self.button = QPushButton("Tanlash")
        self.grid.addWidget(self.button, 2, 1, 1, 2)
        self.button.clicked.connect(self.chiqar)
        
        self.setLayout(self.grid)
        self.show()
        
    def chiqar(self):
        ism = random.choice(self.list)
        self.text.setText(ism)
        

l = [
    "Husan Avazov",
    "Jasur Ahrorov",
    "Malika Shirova",
    "Sardor Komilov",
    "Dilnoza Toirova",
    "Otabek Isoqov",
    "Zilola Karimova",
    "Farruh Olimov",
    "Madina Yusupova",
    "Diyorbek Rustamov",
    "Shahzoda Ergasheva",
    "Anvar Erkinov"
]
app = QApplication([])
m = MainWin(l)
app.exec_()
