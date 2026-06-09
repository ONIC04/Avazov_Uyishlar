print('\033[2J\033[3J\033[H', end='')

# 6-masala. O'quv Markazi
# Kurs classi yarating. Atributlari: nomi, davomiylik, talabalar=[].
# talaba_qoshish(ism) - talaba qo'shadi.
# talabalar_soni() - nechta talaba borligini qaytaradi.
# Kurs obyektini yarating, 3 ta talaba qo'shing va umumiy sonini chiqaring.

class Kurs:
    def __init__(self, n, d):
        self.nomi = n
        self.davomiylik = d
        self.talabalar = []
    def talaba_qushish(self, s):
        self.talabalar.append(s)
        
    def talaba_soni(self):
        return len(self.talabalar)
    
k = Kurs(input("Kurs nomi: "), int(input("Qancha oy davom ettadi: ")))
n = int(input("Nechta talaba qo'shasiz: "))
for i in range(n):
    s = input(f"{i+1} - Talaba ismi: ")
    k.talaba_qushish(s)
print("Talablar qo'shildi")

print()
print(f"Talabalar soni: {k.talaba_soni()}") # yoke shu yerga n ni qo'yish 
print()


