class poling ():
    def voting (self):
        ransel = []
        selempang = []
        tambahan = "iya"
        while tambahan == "iya":
            print ("list pilihan tas yang di gunakan")
            print("1. ransel ")
            print("2. selempang")
            vote = int(input("masukan pilihan (1/2) : "))
            if vote == 1:
                ransel.append(1)
            elif vote == 2:
                selempang.append(1)
            else:
                print("pilihan anda salah")
            tambahan = input("apakah ada tambahan tas iya atau tidak: ")

p1 = poling()
p1.voting()

            

        
        


