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
print('\033[2J\033[3J\033[H', end='')

class User:
    def __init__(self, username: str) -> None:
        self.user = username
        self.__friends = []
        
    def add_friend(self, friend: str) -> bool:
        if friend in self.__friends:
            return False
        else:
            self.__friends.append(friend)
            return True
    
    def remove_friend(self, friend: str) -> bool:
        if friend in self.__friends:
            self.__friends.remove(friend)
            return True
        else: 
            return False
    
    def list_friends(self) -> list[str]:
        if len(self.__friends) >= 1:
            return self.__friends
        else: 
            return []
    
    def is_friend(self, friend: str) -> bool:
        if friend in self.__friends:
            return True
        else:
            return False
    
    def mutual_friends(self, other_user: 'User') -> list[str]:
        s = set(self.__friends) & set(other_user.__friends)
        return list(s)

user1 = User("Ali")
user2 = User("Vali")

print(user1.add_friend("Sami"))    # True
print(user1.add_friend("Vali"))    # True
print(user1.add_friend("Sami"))    # False (allaqachon mavjud)

print(user2.add_friend("Ali"))     # True
print(user2.add_friend("Sami"))    # True

print(user1.list_friends())   # ['Sami', 'Vali']
print(user2.list_friends())    # ['Ali', 'Sami']

print(user1.is_friend("Vali"))     # True
print(user1.is_friend("Botir"))    # False

print(user1.mutual_friends(user2)) # ['Sami']

print(user1.remove_friend("Vali")) # True
print(user1.remove_friend("Botir"))# False
print(user1.list_friends())        # ['Sami']