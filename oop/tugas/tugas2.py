
class gragih():
    def __init__(self,dn,berkembang_biak):
        print("ini adalah tumbuhan gragih")
        self.daun = dn
        self.berkembang_biak = berkembang_biak

    def berkembang(self):
        print(f"kacang tanah  berdaun {self.daun} berkembang secara {self.berkembang_biak} ")
        
class kacang_tanah():

    def __init__(self,dn,berkembang_biak):
        print("ini adalah tumbuhan kacang tanah ")
        self.daun = dn
        self.berkembang_biak = berkembang_biak

    def berkembang(self):
        print(f"kacang tanah  berdaun {self.daun} berkembang secara {self.berkembang_biak} ")

p1 = gragih("berbentuk love","generatif")
p2 = kacang_tanah("bersirip 6","vegetatif")
p1.berkembang()
p2.berkembang()


        

