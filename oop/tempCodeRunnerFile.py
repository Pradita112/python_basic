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