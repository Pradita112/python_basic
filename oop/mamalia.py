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
p1.setAlatpernafasan('insang')
print('p1 bernafasdengan', p1.getAlatpernafasan())
