nama= input("MASUKAN NAMA : ")



nilai1= float(input("masukan nilai biologi: "))
nilai2= float(input("masukan nilai matematika: "))
nilai3= float(input("masukan nilai fisika: "))
nilai4= float(input("masukan nilai kimia: "))
total= (nilai1+nilai2+nilai3+nilai4)/4

if nilai1 == 80 and total >=70:
    print("anda lulus beasiswa")
elif nilai2 == 80 and total >=60:
    print("anda lulus beasiswa")
elif nilai3 == 80 and total >=60:
    print("anda lulus beasiswa")
elif nilai4 == 80 and total >=60:
    print("anda lulus beasiswa")
else:
    print ("anda belum lulus")