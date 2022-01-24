tarik = float(input("masukan uang yang akan di ambil : "))
saldo = 250000

if tarik%50000 == 0:
    print("transaksi berhasil")
    print(f"jumlah penarikan : {tarik}")
    print (f"sisa saldo adalah : {saldo-tarik}")
else:
    print("nominal yang anda masukan salah")
        
