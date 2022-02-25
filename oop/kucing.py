
class Kucing():
    jenis = ""
    makanan = ""

    def __init__(self,jns,mkn):
        print('ini adalah kucing')
        self.jenis = jns
        self.makanan = mkn

    def makan(self):
        print(f"kucing jenis {self.jenis}makan {self.makanan}")
    
k1= Kucing('persia','udang')
k1.makan()
k2 = Kucing('lokal',"butiran")
k2.makan()



