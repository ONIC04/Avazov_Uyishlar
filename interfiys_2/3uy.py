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
#from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

stil_oyna = "background-color: #0b2e3b; color: #14991f"
stil_button = "font-size: 25px; color: red;"
app = QApplication([])
class Kalkulyator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Hisoblagich")
        self.setStyleSheet(stil_oyna)
        self.grid = QGridLayout()
        
        self.line = QLineEdit()
        self.line.setPlaceholderText("son1...")
        self.grid.addWidget(self.line, 1, 1)
        
        self.line1 = QLineEdit()
        self.line1.setPlaceholderText("son2...")
        self.grid.addWidget(self.line1, 1, 2)
        
        self.text = QLabel("=")
        self.grid.addWidget(self.text, 1, 3)
        
        self.natija = QLabel("0")
        self.grid.addWidget(self.natija, 1, 4)
        
        self.button1 = QPushButton("*")
        self.button1.setStyleSheet(stil_button)
        self.grid.addWidget(self.button1, 2, 1)
        self.button1.clicked.connect(self.kup)
        
        self.button2 = QPushButton("÷")
        self.button2.setStyleSheet(stil_button)
        self.grid.addWidget(self.button2, 2, 2)
        self.button2.clicked.connect(self.bulish)
        
        self.button3 = QPushButton("-")
        self.button3.setStyleSheet(stil_button)
        self.grid.addWidget(self.button3, 2, 3)
        self.button3.clicked.connect(self.ayir)
        
        self.button4 = QPushButton("+")
        self.button4.setStyleSheet(stil_button)
        self.grid.addWidget(self.button4, 2, 4)
        self.button4.clicked.connect(self.qush)
        
        self.setLayout(self.grid)
        self.show()
        
    def kup(self):
        son1 = int(self.line.text())
        son2 = int(self.line1.text())
        natija = son1 * son2
        self.natija.setText(str(natija))
    
    def bulish(self):
        son1 = int(self.line.text())
        son2 = int(self.line1.text())
        natija = son1 / son2
        self.natija.setText(str(natija))
    
    def ayir(self):
        son1 = int(self.line.text())
        son2 = int(self.line1.text())
        natija = son1 - son2
        self.natija.setText(str(natija))
    
    def qush(self):
        son1 = int(self.line.text())
        son2 = int(self.line1.text())
        natija = son1 + son2
        self.natija.setText(str(natija))

k = Kalkulyator()
app.exec_()