laki=[]
perempuan=[]
daftar = "iya"
while daftar == "iya":
    nama= input("masukan nama : ")
    umur = input("masukan umur : ")
    gender = input("masukan gender l/p : ")
    if gender == "l":
        laki.append(nama)
    else:
        perempuan.append(nama)
    print ("masih ada lagi yang daftar iya/tidak ")
    daftar = input()
    if daftar != "iya":
        break
    else:
        pass
print ("ini kost laki",laki)
print("ini kos perempuan",perempuan)

