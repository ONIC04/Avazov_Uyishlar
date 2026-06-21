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
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QGridLayout,)
#from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

stil_oyna = "background-color: #0b2e3b; color: #14991f"
stil_rang = "font-size: 30px; color: red;"
colors = [
    "Red", "Blue", "Green", "Yellow", "Black", 
    "White", "Orange", "Purple", "Pink", "Brown", 
    "Gray", "Cyan", "Magenta", "Silver", "Gold", 
    "Maroon", "Navy", "Olive", "Teal", "Beige"
]

app = QApplication([])
class Ranglar(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Random rang")
        self.setStyleSheet(stil_oyna)
        self.grid = QGridLayout()
        
        self.text = QLabel("Faundasion N204")
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setStyleSheet("font-weight: bold;")
        self.grid.addWidget(self.text, 1, 1, 1, 2)
        
        self.button = QPushButton("Rang")
        self.button.setStyleSheet(stil_rang)
        self.grid.addWidget(self.button, 2, 1, 1, 2)
        self.button.clicked.connect(self.alish)
        
        self.setLayout(self.grid)
        self.show()
        
    def alish(self):
        rang = random.choice(colors)
        self.text.setStyleSheet(f"font-weight: bold; color: {rang}")
        
        
r = Ranglar()
app.exec_()
        
        