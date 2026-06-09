print('\033[2J\033[3J\033[H', end='')

# 7-masala. Kutubxona tizimi. Bu masalada ikkita classni o'zaro bog'lab ishlatishingiz kerak bo'ladi.
# Kitob classi yarating (nomi, muallif).
# Kutubxona classi yarating:
# Atributlari: kitoblar (list) - kitoblar ro'yxatini o'zida saqlaydi.
# kitob_qoshish(kitob) - kitob obyektini qo'shadi.
# qidirish(nom) - nomi bo'yicha kitobni qidiradi.
# Kutubxonaga bir nechta kitob qo'shib, ulardan birini qidirib toping.

class Kitob:
    def __init__(self, nom, muallif):
        self.nom = nom
        self.muallif = muallif

class Kutubxona:
    def __init__(self):
        self.kitoblar = []

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)

    def qidirish(self, nom):
        for kitob in self.kitoblar:
            if kitob.nom.lower() == nom.lower(): 
                return f"Topildi: '{kitob.nom}' — {kitob.muallif}"
        return "Kitob topilmadi!"

k1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy")
k2 = Kitob("Mehrobdan chayon", "Abdulla Qodiriy")
k3 = Kitob("Sariq devni minib", "Xurshid Davron")

lib = Kutubxona()
lib.kitob_qoshish(k1)
lib.kitob_qoshish(k2)
lib.kitob_qoshish(k3)

nom = input("Kitob nomini kiriting: ")
print(lib.qidirish(nom))


