print('\033[2J\033[3J\033[H', end='')

# 4-masala. Bank Hisobi
# BankHisob classi yarating. Atributlari: ism, balans=0.
# deposit(summa) - balansni oshiradi.
# yechib_ol(summa) - balansni kamaytiradi (agar yetarli bo'lsa).
# hisob() - hozirgi balansni qaytaradi.
# Hisob oching, unga 1000 qo'shing, 400 yeching.

class BankHisob:
    def __init__(self, i, b = 0):
        self.ism = i
        self.balans = b
        
    def deposit(self, summa):
        self.balans += summa
    
    def yechib_ol(self, summa):
        if self.balans >= summa:
            self.balans -= summa
            print("Hozirgi balans", self.hisob())
        else:
            print(f"Balansda yetarli mablag' mavjud emas: Balns - {self.balans}")
    def hisob(self):
        return self.balans
    
b = BankHisob("Random")
b.deposit(1000)
b.yechib_ol(400)
