
class ikan():
    __jenis = "mujaer"
    makanan = "pelet"
    __bernafas = "insang"

    def __init__(self):
        print(f"ikan jenis {self.__jenis} makan {self.makanan} bernafas {self.__bernafas}")

    def getjenis(self):
        return self.__jenis
    def setjenis(self,jenis_ikan):
        self.__jenis = jenis_ikan


p1 = ikan()
print(p1.getjenis())
p1.setjenis("koi")
print(p1.getjenis())





    






