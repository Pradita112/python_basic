hargabarang = float(input("masukan total belanjaan " ))

if hargabarang > 100000:
    diskon = hargabarang * 20/100
    total = hargabarang - diskon
    print(f"anda mendapatkan diskon 20% karena berbelanja lebih dari 100000")
    print(f"total belanja anda : {total}")
else:
    print(f"total belanja anda {hargabarang}")