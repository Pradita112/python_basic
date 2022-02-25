def bmi():
    nama= input("masukan nama : ")
    umur = input("masukan umur : ")
    bb= int(input('masukan berat badan: '))
    tb= int(input('masukan tinggi badan: '))
    bmii= bb/(tb*tb)
    print(f"hasil imt nya adalh : {bmii}")
    if bmii < 17:
        print("kekurangan berat badan")
    elif bmii >= 17 and bmii <= 18.4:
        print("kekurangan berat badan")
    elif bmii >= 18.5 and bmii <= 25:
        print("normal")
    elif bmii >= 26 and bmii <= 27:
        print("gemuk")
    elif bmii > 27:
        print("gemuk")
    
  
bmi()

    
