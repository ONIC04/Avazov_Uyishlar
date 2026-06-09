print('\033[2J\033[3J\033[H', end='')

# 2-masala. Kitob Classi
# Kitob classi bo'lsin. Atributlari: nomi, muallif, sahifa_soni.
# qisqacha() metodi kitob haqida qisqa malumot qaytarsin.
# katta_kitobmi() metodi sahifa soni 300 dan ko'p bo'lsa True, bo'lmasa False qaytarsin.

class Kitob:
    def __init__(self, n, m, sn):
        self.nomi = n
        self.mualif = m
        self.sahifa_soni = sn
    
    def qisqacha(self):
        return self.nomi, self.mualif
    def katta_kitobmi(self):
        if self.sahifa_soni > 300:
            return True
        else:
            return False
    
k = Kitob(input("Kitob nomi: "), input("Kitob mualifi: "), int(input("Sahifa soni: >>> ")))
javob = k.qisqacha()
print(f"{javob[1]}: {javob[0]} <- - -> katta kitobmi: {k.katta_kitobmi()}")



