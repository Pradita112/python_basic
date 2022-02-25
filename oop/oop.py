#blue print
from mimetypes import init
from typing_extensions import Self


class Medusa():
    name = 'medusa'
    role = 'carry'
    wepom = 'bow'
    def stun():
        print('stun')
#instance
m1 = Medusa()
m2 = Medusa()
#acces atribut
print(f"nama object pertama {m1.name}")
print(f"nama object pertama {m2.name}\n")
#change attribut
m2.name = 'juggernaut'
print(f"m1.n{m1.name}")
print(f"m2.n{m2.name}\n")
class Kucing():
    jenis = ""
    asal = ""
    def makan(self):
        print(f"kucing jenis {self.jenis} makan {self.makan}")
    
k = Kucing()
print(f"asal kucing {k.asal}")
print(f"jenis kucing {k.jenis}\n")

class Labalaba():
    jenis = "tarantula"
    asal = "itali"

    def jaring():
        print("mengeluarkan jaring")

L = Labalaba()
print(f"asal laba-laba {L.asal}")
print(f"jenis laba-laba {L.jenis}\n")

class Kangguru():
    jenis = "nabarlek"
    asal = "australia"
    def melompat():
        print("melompat")
ka = Kangguru()
print(f"asal kangguru {ka.asal}")
print(f"jenis kangguru {ka.jenis}")

class mamalia():
    __alat_pernafasan = 'paru-paru'
    nama = ''

    def __init__(self):
        print("ini adalah mamalia")

    def getAlatpernafasan(self):
        return self.__alat_pernafasan

    def setAlatpernafasan(self, alat_pernafasan):
        self.__alat_pernafasan = alat_pernafasan
p1 = mamalia()
print('p1 bernafasdengan', p1.getAlatpernafasan())

