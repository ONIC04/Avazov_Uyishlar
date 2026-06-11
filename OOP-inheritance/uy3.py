#import math
#import requests
#import random
#import datetime
#import os, sys
#import time
#import pytz
#import json
# from deep_translator import GoogleTranslator as tarjimon
#from collections import Counter, defaultdict
print('\033[2J\033[3J\033[H', end='')

# User(Foydalanuvchi) nomli class yarating(name, username, followers (list), following (list) kabi attributelari bilan).
# Bu classga follow (followingga yangi element qo'shish), unfollow (followingdan element o'chirish) va
# remove_follower(followersdan element o'chirish) nomli metodlar yozing.

class User:
    def __init__(self, n, us, fs: list, fng: list):
        self.name = n
        self.username = us
        self.followrs = fs
        self.following = fng
        
class Instagram(User):
    def __init__(self, n, us, fs, fng):
        super().__init__(n, us, fs, fng)
        
    def follow(self, s):
        """Followingga elment qo'shish"""
        self.following.append(s)
    
    def unfollow(self, s: str):
        """Followingdan element o'chirish"""
        for i in self.following:
            if i.lower() == s.lower():
                self.following.remove(i)
                break
    
    def remove_followers(self, s: str):
        """Followersdan element O'chirish"""
        for i in self.followrs:
            if i.lower() == s.lower():
                self.followrs.remove(i)
                break

na = input("Name: ")
usna = input("User name: ")
n = int(input("Nechata followers: "))
n1 = int(input("Nechta following: "))
l = []
l1 = []
print("\nFollwers Qo'shilmoqda...\n")
for i in range(n):
    s = input(f"{i+1} - Ism: ")
    l.append(s)
print("\nFollowing Qo'shilmoqda...\n")
for i in range(n1):
    s = input(f"{i+1} - Ism: ")
    l1.append(s)
print("\n\t\tJarayonlar tugatildi tanlang«««\n")    
o = Instagram(na, usna, l, l1)
while 1:
    try:
        print("1- Following qo'shish\n2- Unfollowing\n3- Remove followers")
        t = int(input(">>> "))
        if t==1:
            nn = int(input("Nechta following qo'shashiz: "))
            for i in range(nn):
                o.follow(s = input(f"{i+1} - Ism: "))
            print("Followinga Qo'shsih tugatildi...")
            print("\n\t\tFollowing's\n")
            for i in o.following:
                print(i)
            print()
            break
        elif t==2:
            s = input("\nFollowingdan o'chirasiz ism: ")
            print()
            o.unfollow(s)
            print(f"{s} O'chirldi")
            print("\n\t\tFollowing's\n")
            for i in o.following:
                print(i)
            print()
            break
        elif t==3:
            s = input("\nFollowrsdan o'chirasiz ism: ")
            print()
            o.remove_followers(s)
            print(f"{s} O'chirldi")
            print("\n\t\tFollowing's\n")
            for i in o.followrs:
                print(i)
            print()
            break
        else:
            print("Xato tanlov qayta kiriting!")
        print()
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        