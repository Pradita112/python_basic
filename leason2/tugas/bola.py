cuaca =input("kondisi lapangan hujan atau terang ")
lapangan=input("kondisi lapangan becek atau tidak  :")

if cuaca == "terang" and lapangan== "kering":
    print("kita dapat bermain bola tanpa dengan sepatu")
else:
    if cuaca == "terang" and lapangan == "becek":
        print("kita dapat bermain bola dengan spatu")
    else:
        print ("kita tidak dapat bermain bola")

    


