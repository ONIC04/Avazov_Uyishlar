from math import sqrt as ildiz
print('\033[2J\033[3J\033[H', end='')

# 5-masala. Uchburchak Classi
# Uchburchak classi yarating. Uch tomon: a, b, c.
# perimetr() metod - perimetrni qaytaradi.
# maydon() metod - Heron formulasidan foydalanib maydon hisoblaydi.
# Uchburchak classidan obyekt yarating va uning perimetri va maydonini hisoblang.

class Uchburchak:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetr(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return self.a + self.b + self.c
        else: 
            return None
    
    def maydon(self):
        p = self.perimetr()
        if p is None:
            print("Bu tomonlar bilan uchburchak yasab bo'lmaydi!")
            return None
        s = p / 2
        return ildiz(s * (s-self.a) * (s-self.b) * (s-self.c))
    
    
u = Uchburchak(int(input("a = ")), int(input("b = ")), int(input("c = ")))
print(f"Uchburchak perimetri: {u.perimetr()}")
print(f"Uchburchak maydoni: {u.maydon()}")


        


