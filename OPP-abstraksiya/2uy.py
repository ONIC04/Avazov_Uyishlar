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

class Employee:
    def __init__(self, name: str, employee_id: str, hourly_rate: float = 15.0):
        self.name = name
        self.employee_id = employee_id
        self.__working_hours = []
        self.hourly_rate = hourly_rate
        
    def log_hours(self, hour: int) -> bool:
        if 0 < hour <= 24:
            self.__working_hours.append(hour)
            return True
        else:
            return False
    
    def total_hours(self) -> int:
        return sum(self.__working_hours)
    
    def calculate_salary(self) -> float:
        return sum(self.__working_hours) * self.hourly_rate
    
    def reset_hours(self) -> None:
        self.__working_hours = []
        

employee = Employee("Javlon", "E101", hourly_rate=20.0)

print(employee.log_hours(8))   	# True
print(employee.log_hours(9))   	# True
print(employee.log_hours(10))  	# True
print(employee.log_hours(25))  	# False 

print(employee.total_hours())       	# 27
print(employee.calculate_salary())  	# 540.0 (27 * 20)

employee.reset_hours()
print(employee.total_hours())       	# 0
print(employee.calculate_salary())  	# 0.0
        