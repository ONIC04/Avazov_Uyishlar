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
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,QComboBox, QCheckBox, QGridLayout)
#from PyQt5.QtCore import QTimer
#from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

# 2-masala. Oyma-oy byudjet nazorati
# Har bir oy uchun xarajatlar ro'yxati dictda saqlanadi:
# {"Yanvar": [1200000, 500000], "Fevral": [2000000, 800000]}
# Foydalanuvchi oynada oy nomini tanlasa, shu oyning umumiy xarajati hisoblab chiqarilsin.

class MainWindow(QWidget):
    def __init__(self, m):
        super().__init__()
        self.moliya = m
        self.grid = QGridLayout()
        self.setWindowTitle("Nazotar")
        
        l = ["Tanla"]
        for i in self.moliya:
            l.append(i)
        self.cbox = QComboBox()
        self.cbox.addItems(l)
        self.grid.addWidget(self.cbox, 1, 1)
        
        self.text = QLabel("Natija")
        self.text.setStyleSheet("color: green")
        self.grid.addWidget(self.text, 1, 2)
        
        self.button = QPushButton("Hisobla")
        self.button.setStyleSheet("background-color: red")
        self.grid.addWidget(self.button, 2,1,1,2)
        self.button.clicked.connect(self.hisoblash)
    
        self.setLayout(self.grid)
        self.show()
    def hisoblash(self):
        oy = self.cbox.currentText()
        if oy == None or oy == "Tanla":
            self.text.setText("Iltimos oy tanlang!")
            self.text.setStyleSheet("color: red")
        else:
            natija = sum(self.moliya[oy])
            self.text.setText(str(natija))
            self.text.setStyleSheet("color: green")
            
    
moliya = {
    "Yanvar": [1286405, 136110, 2344044, 2149360, 1156580],
    "Fevral": [830387, 886076, 2854381],
    "Mart": [2941018],
    "Aprel": [1509835, 896254],
    "May": [542189, 1953129, 900180],
    "Iyun": [1222275, 1451223, 2243337],
    "Iyul": [2962666, 2573492, 2042263, 702517],
    "Avgust": [1757955, 1278907, 586213, 884834, 1369708],
    "Sentyabr": [128720, 1232925, 982540],
    "Oktyabr": [479412, 1404197, 953859, 1092581],
    "Noyabr": [2886774, 1805387],
    "Dekabr": [2925919, 1426223, 2292549],
}  
app = QApplication([])
m = MainWindow(moliya)
app.exec_()



