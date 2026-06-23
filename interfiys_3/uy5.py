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

# 5-masala. Dars jadvali
# dictda dars jadvali saqlansin saqlansin:
# {"Dushanba": ["Matematika", "Fizika"], "Seshanba": ["Ingliz tili", "Tarix"]}
# Foydalanuvchi kun tanlasa, shu kunga oid darslar ro'yxati chiqsin.

class MainWindow(QWidget):
    def __init__(self, d: dict):
        super().__init__()
        self.jadval = d
        self.setWindowTitle("Maktab")
        self.grid = QGridLayout()
        
        l = []
        for i in self.jadval:
            l.append(i)
        self.cbox = QComboBox()
        self.cbox.addItems(l)
        self.grid.addWidget(self.cbox, 1, 1, 1, 2)
        
        self.button = QPushButton("Darslar")
        self.grid.addWidget(self.button, 2, 1, 1, 2)
        
        self.mm = QLabel("Fan nomi")
        self.grid.addWidget(self.mm, 3, 1, 1, 2)
        self.button.clicked.connect(self.chiqarish)
        
        self.m = QLabel("Shu yerda darslar chiqadi!")
        self.grid.addWidget(self.m, 4, 1, 1, 2)
        
        
        
        self.setLayout(self.grid)
        self.show()
        
    def chiqarish(self):
        fan = self.cbox.currentText()
        self.mm.setText(fan)
        darslar = self.jadval.get(fan, [])
        self.m.setText(", ".join(darslar))
    
    
    
jadval = {
  "Dushanba": ["Matematika", "Fizika", "Ona tili"],
  "Seshanba": ["Ingliz tili", "Tarix", "Kimyo"],
  "Chorshanba": ["Biologiya", "Geografiya", "Informatika"],
  "Payshanba": ["Matematika", "Adabiyot", "Rus tili"],
  "Juma": ["Fizika", "Jismoniy tarbiya", "Chizmachilik"],
  "Shanba": ["Texnologiya", "Astronomiya"]
}

app = QApplication([])
m = MainWindow(jadval)
app.exec_()