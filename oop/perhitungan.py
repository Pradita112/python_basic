
class perhitungan():
    hasil:int = 0
    hk:int = 0

    def tambah(self,a:int, b:int):
        self.hasil = a+b

    @classmethod
    def kurang(cls,a:int,b:int):
        cls.hk = a - b

    @staticmethod
    def luas_segitiga(a,t):
        return 1/2*a*t

    @staticmethod
    def luas_balok(p,l):
        return p*l

seg = perhitungan.luas_segitiga(10,5)
bal = perhitungan.luas_balok(10,2)
print(f"segitiga {seg} -- balok {bal}")

p1 = perhitungan()
p1.tambah(10,2)
p1.kurang (10,5)

print(f"hasil tmbah {p1.hasil}")
print(f"hasil kurang {p1.hk}")


