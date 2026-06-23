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

# 3-masala. Ofis xodimlari
# dictda xodimlarning ismi va lavozimi saqlanadi:
# { "Dilshod": "Direktor", "Aziza": "Hisobchi" }
# PyQt5 oynasida ism LineEdit orqli ism kiritiladi, sizning vazifangiz xodimning lavozimini ko'rsatish. Qo'shimcha qilib, yangi xodim qo'shish imkoniyatini ham qo'shing

class Nazorat(QWidget):
    def __init__(self, oldingi_oyna, x: dict):
        super().__init__()
        self.oldngi = oldingi_oyna
        self.xodimlar = x
        self.setWindowTitle("Xodimlarni nazorat qilish")
        self.grid = QGridLayout()
        
        self.line = QLineEdit()
        self.line.setPlaceholderText("ismi...")
        self.grid.addWidget(self.line, 1, 1)
        
        self.line1 = QLineEdit()
        self.line1.setPlaceholderText("Lavozim...")
        self.grid.addWidget(self.line1, 1, 2)
        
        self.cbox = QComboBox()
        self.cbox.addItems(["Tanlav", "Qo'shish", "Ketqazish"])
        self.grid.addWidget(self.cbox, 2, 1, 1, 2)
        
        self.m = QLabel("Natija shu yerda chiqadi!")
        self.m.setStyleSheet("color: red;")
        self.grid.addWidget(self.m, 3, 1, 1, 2)
        
        self.button = QPushButton("Bajar")
        self.button.setStyleSheet("background-color: #be1ac7;")
        self.grid.addWidget(self.button, 4, 1, 1, 2)
        self.button.clicked.connect(self.bajar)
        
        self.button2 = QPushButton("Asasiy oyna")
        self.button2.setStyleSheet("background-color: green;")
        self.grid.addWidget(self.button2, 5, 1, 1, 2)
        self.button2.clicked.connect(self.back_main)
        
        self.setLayout(self.grid)
        
    def back_main(self):
        self.oldngi.show()
        self.hide()
        
    def bajar(self):
        ism = self.line.text().strip()
        lavozim = self.line1.text().strip()
        tanlov = self.cbox.currentText()

        if not ism or not lavozim:
            self.m.setText("Iltimos ism va lavozim majburiy!")
            self.m.setStyleSheet("color: red;")
            return

        if tanlov == "Tanlav":
            self.m.setText("Iltimos tanlov qiling!")
            self.m.setStyleSheet("color: red;")
            return

        if tanlov == "Qo'shish":
            self.xodimlar[ism] = lavozim
            self.m.setText(f"'{ism}' muvaffaqiyatli qo'shildi/yangilandi!")
            self.m.setStyleSheet("color: green;")
        else:
            topildi = False
            for kalit in list(self.xodimlar):
                if kalit.lower() == ism.lower():
                    self.xodimlar.pop(kalit)
                    topildi = True
                    break
            if topildi:
                self.m.setText(f"'{ism}' o'chirildi!")
                self.m.setStyleSheet("color: green;")
            else:
                self.m.setText("Bunday xodim topilmadi!")
                self.m.setStyleSheet("color: red;")
                        
     

class MainWindow(QWidget):
    def __init__(self, x: dict):
        super().__init__()
        self.xodimlar = x
        self.grid = QGridLayout()
        
        self.line = QLineEdit()
        self.line.setPlaceholderText("Xodim ismi...")
        self.grid.addWidget(self.line, 1, 1, 1, 2)
        
        self.m = QLabel("Lavozim shu yerda chiqadi!")
        self.m.setStyleSheet("color: red;")
        self.grid.addWidget(self.m, 2, 1, 1, 2)
        
        self.button = QPushButton("Lavozim")
        self.button.setStyleSheet("background-color: #be1ac7;")
        self.grid.addWidget(self.button, 3, 1, 1, 2)
        self.button.clicked.connect(self.natija)
        
        self.button1 = QPushButton("Nazorat")
        self.button1.setStyleSheet("background-color: green;")
        self.grid.addWidget(self.button1, 4, 1, 1, 2)
        self.button1.clicked.connect(self.next_oyna)
        
        self.setLayout(self.grid)
        self.show()
        
    def next_oyna(self):
        self.nazorat = Nazorat(self, self.xodimlar)
        self.nazorat.show()
        self.hide()
        
    def natija(self):
        ism = self.line.text()
        t = 0
        for k, q in self.xodimlar.items():
            if k.lower() == ism.lower():
                self.m.setText(q)
                self.m.setStyleSheet("color: #c75c1a;")
                t = 1
                break
        if t == 0:
            self.m.setText("Xodim topilmadi Nazoratdn qo'shing!")
            self.m.setStyleSheet("color: red;")
                
        
        
        



xodimlar = {
    "Dilshod": "Direktor",
    "Aziza": "Hisobchi",
    "Jasur": "Dasturchi",
    "Malika": "Marketolog",
    "Bekzod": "Sotuv menejeri",
    "Nodira": "Kadrlar bo'limi boshlig'i",
    "Sardor": "Tizim administratori",
    "Gulbahor": "Kotiba",
    "Olim": "Omborchi",
    "Shahnoza": "Yurist",
}


app = QApplication([])
m = MainWindow(xodimlar)
app.exec_()