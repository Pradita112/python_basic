class Murid():

    def __init__(self,nama_awal,nama_akhir,beladiri):
        self.nl = nama_awal
        self.na = nama_akhir
        self.bd = beladiri

    def __repr__(self):
        return self.nl + "" + self.na
    
    def description (self):
        print(f"{self.nl} -- {self.na} belajar bela diri {self.bd}")

class Beladiri():

    def __init__(self,bela_diri:str):
        self.bd = bela_diri

    def __repr__(self):
        return self.name

p1 = Murid("pradita","dwi","kempo")
p2= Beladiri("kempo")
p1.description()

