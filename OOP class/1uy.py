print('\033[2J\033[3J\033[H', end='')

# 1-masala. Do'kon Mahsuloti
# Mahsulot classi yarating. Atributlari: nom, narx, miqdor.
# sotib_ol(miqdor) metodi chaqirilganda miqdorni kamaytirsin.
# qolgan_miqdor() metodi nechta mahsulot qolganini qaytarsin.
# Bir mahsulotdan obyekt yarating, undan 2 marta sotib oling.

class Mahsulot:
    def __init__(self, nom, narx, miqdor):
        self.nom = nom
        self.narx = narx
        self.miqdor = miqdor
        
    def sotib_ol(self, i):
        print(f"{i} - marta: Maxsulot miqdori: ", self.miqdor)
        n = int(input("Nechta sotib olasz: "))
        if self.miqdor >= n:
            self.miqdor -= n
        else:
            print("Siz miqdordan ko'p maxshulot sotib olmoqchisiz!")
    
    def qolgan_miqdor(self):
        return self.miqdor


m = Mahsulot(input("Mahsulot nomi: "), float(input("Maxsulot narxi: ")), int(input("Miqdor: ")))
tt = int(input("Necha marta sotib olasiz: "))
for i in range(1, tt+1):
    m.sotib_ol(i)
print("\n\n")
print("<- - ->" * 10)
print()
print(f"Qolgan miqdor {m.qolgan_miqdor()}")
print()
print("<- - ->" * 10)

        
        