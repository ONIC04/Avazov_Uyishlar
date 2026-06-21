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
from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

stil_oyna = "background-color: #0b2e3b; color: #14991f"
app = QApplication([])
class Malumot(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Ma'lumot")
        self.setStyleSheet(stil_oyna)
        self.grid  = QGridLayout()
        
        self.text = QLabel("")
        self.text.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.text, 1, 1, 1, 2)
        
        self.button = QPushButton("Ism")
        self.grid.addWidget(self.button, 2, 1, 1, 2)
        self.button.clicked.connect(self.button_1)
        
        self.button1 = QPushButton("Familiya")
        self.grid.addWidget(self.button1, 3, 1, 1, 2)
        self.button1.clicked.connect(self.button_2)
        
        self.button2 = QPushButton("Tug'ilgan yil")
        self.grid.addWidget(self.button2, 4, 1, 1, 2)
        self.button2.clicked.connect(self.button_3)
        
        
        self.setLayout(self.grid)
        self.show()
        
    def button_1(self):
        self.text.setText("Husan")
    
    def button_2(self):
        self.text.setText("Avazov")
    
    def button_3(self):
        self.text.setText("2004.12.09")
        
        
m = Malumot()
app.exec_()