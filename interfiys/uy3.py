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
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit)
#from PyQt5.QtCore import QTimer
#from PyQt5.QtGui import QFont
print('\033[2J\033[3J\033[H', end='')

# 2 ta LineEdit orqali ikkita sonni oling. Oynaga to'rtta tugmacha qo'shing
# ("Qo'shish", "Ayirish", "Ko'paytirish", "Bo'lish"). Shu tugmachalar bosilganda,
# kiritilgan ikkita son o'rtasida mos amalni bajarib javobini labelga chiqaruvchi dastur tuzib.

"""Avval ikki son linelarga kiritib kiyin amal bosilsa natijani chiqazib beradi"""
px = 38
lin1_x = round(px * 2.4)
teng_x = round(px * 3.7)
javob_x = round(px*4.3)
app = QApplication([])

oyna = QWidget()

oyna.setWindowTitle("4 amal kalkulyator")
oyna.setGeometry(0, 0, px*6, px*10)
oyna.setStyleSheet("background-color: #012422")

line = QLineEdit(oyna)
line.setPlaceholderText("son1")
line.setStyleSheet("background-color: #91ede9; color: black;")
line.setGeometry(px, px, px, px)

line1 = QLineEdit(oyna)
line1.setPlaceholderText("son2")
line1.setStyleSheet("background-color: #91ede9; color: black;")
line1.setGeometry(lin1_x, px, px, px)

teng = QLabel(oyna)
teng.setText("=")
teng.setGeometry(teng_x, px, px, px)
teng.setStyleSheet("font-size: 20px; color: red;")

javob = QLabel(oyna)
javob.setText("0")
javob.setGeometry(javob_x, px, px*2, px)
javob.setStyleSheet("font-size: 25px; color: red; font-weight: bold; color: #91ede9; border: 2px solid black;")

kup = QPushButton(oyna)
kup.setText("*")
kup.setGeometry(px, px *3, px*2, px *2)
kup.setStyleSheet("font-size: 20px; background-color: #91ede9; color: red")

bulish = QPushButton(oyna)
bulish.setText("÷")
bulish.setGeometry(px, px *5, px*2, px *2)
bulish.setStyleSheet("font-size: 20px; background-color: #91ede9; color: red")

ayirish = QPushButton(oyna)
ayirish.setText("-")
ayirish.setGeometry(px, px *7, px*2, px *2)
ayirish.setStyleSheet("font-size: 20px; background-color: #91ede9; color: red")

qushish = QPushButton(oyna)
qushish.setText("+")
qushish.setGeometry(px*3, px *3, px*2, px *6)
qushish.setStyleSheet("font-size: 20px; background-color: #91ede9; color: red")

def bos():
    son1 = int(line.text())
    son2 = int(line1.text())
    natija = son1 * son2
    javob.setText(str(natija))
kup.clicked.connect(bos)

def bos1():
    son1 = int(line.text())
    son2 = int(line1.text())
    natija = son1 // son2
    javob.setText(str(natija))
bulish.clicked.connect(bos1)

def bos2():
    son1 = int(line.text())
    son2 = int(line1.text())
    natija = son1 - son2
    javob.setText(str(natija))
ayirish.clicked.connect(bos2)

def bos3():
    son1 = int(line.text())
    son2 = int(line1.text())
    natija = son1 + son2
    javob.setText(str(natija))
qushish.clicked.connect(bos3)


oyna.show()
app.exec_()