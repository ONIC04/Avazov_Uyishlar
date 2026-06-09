print('\033[2J\033[3J\033[H', end='')

# 3-masala. Avtomobil
# Avtomobil classi tuzing. Atributlari: model, yil, tezlik.
# tezlashtir() - tezlikni +10 oshiradi.
# sekinlashtir() - tezlikni -10 kamaytiradi.
# info() - avtomobil model, yil va tezligini chiqaradi.
# Avtomobilni 3 marta tezlashtiring, keyin 1 marta sekinlashtiring.

class Avtomobil:
    def __init__(self, m, yil, t):
        self.model = m
        self.yil = yil
        self.tezlik = t
        self.tezlik1 = self.tezlik
    
    def tezlashtir(self, i):
        print(f"{i} - urinishda tezlashtirdi")
        self.tezlik +=10
    
    def sekinlalshtir(self, i):
        print(f"{i} - urinishda sekinlastirildi")
        self.tezlik -= 10
        print(f"Avtomobilning hozirgi tezligi: {self.tezlik}")
    def info(self):
        print(f"{self.model} yili: {self.yil} - tezligi: {self.tezlik1}")
    
    
a = Avtomobil(input("Nomi: "), int(input("Yili: ")), float(input("Tezligi: ")))
for i in range(1, 5):
    if i == 4:
        a.sekinlalshtir(i)
        break
    a.tezlashtir(i)
    
print("\n\n")
print("<- - ->" * 10)
print()
print("Avtomabil haqida malumot")
a.info()
print()
print("<- - ->" * 10) #  --so'ralmagani uchun max tezlikni qo'shib o'tirmadim 
