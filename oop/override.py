class kendaraan:
    def __init__(self,bahan_bakar:str, kapasitas:int):
        self.bb = bahan_bakar
        self.kp = kapasitas
    
    def info(self):
        print("ini adalah kendaraan")
        
class motor(kendaraan):
    def info(self):
        print("ini kendaraan motor")

k = motor('bensin',2)
k.info()

class mamalia:
    def __init__(self,makanan:str, bernafas:str):
        self.bern = bernafas
        self.mkn = makanan
    
    def info(self):
        print("ini adalah hewan mamalia")
    
class kucing(mamalia):
    def info(self):
        print("ini adalah kucing")

k = mamalia('wiskas','paruparu')
k.info()
