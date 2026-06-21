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
from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

stil_oyna = "background-color: #0b2e3b; color: #14991f"
app = QApplication([])
class Sana(QWidget):
    def __init__(self, s = 0):
        super().__init__()
        self.s = s
        
        self.setWindowTitle("Sanagich")
        self.setStyleSheet(stil_oyna)
        self.gred = QGridLayout()
        
        self.text = QLabel("0")
        self.text.setAlignment(Qt.AlignCenter)
        self.gred.addWidget(self.text, 1, 1, 1, 2)
        
        self.button = QPushButton("count")
        self.gred.addWidget(self.button, 2, 1, 1, 2)
        self.button.clicked.connect(self.sanash)
        
        self.setLayout(self.gred)
        self.show()
        
    def sanash(self):
        self.s += 1
        if self.s >= 11:
            self.close()
        son = random.randint(1, 100)
        self.text.setText(str(son))
        
        
        
s = Sana()
app.exec_()
