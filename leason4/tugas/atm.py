pin = 123456

print('selamat datang di atm')
print(10*"**")
size =0

while pin == 123456:
    masukan = int(input("masukan pin anda : "))
    if masukan == pin:
        print("selamat berteansaksi ")
        break
    else:
        print("pin anda salah masukan lagi iya atau tidak :")
        jawab = input()
        size+=1
        if jawab == "iya":
            pass
        else:
            break
    if size == 3:
        print("kartu anda tertelan ")
        break

print (size)

    
    


    
    

