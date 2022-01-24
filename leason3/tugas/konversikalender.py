from pyparsing import And

nomor_tanggal= int(input("masukan nomor tanggal: "))
nomor_bulan= int(input("Masukan nomor bulan: "))

if (nomor_tanggal >= 4 and nomor_bulan ==1) or (nomor_tanggal == 1 and nomor_bulan==2):
    print(nomor_tanggal>4<32)
    print("jumadil-akhirah")
elif (nomor_tanggal >= 2 and nomor_bulan == 2 ) or (nomor_tanggal<= 3 and nomor_bulan ==3):
    print("rajab") 
elif (nomor_tanggal >= 4 and nomor_bulan == 3) or (nomor_tanggal<=2 and nomor_bulan== 4):
    print("sya'ban")
elif (nomor_tanggal >= 3 and nomor_bulan == 4) or (nomor_tanggal ==1 and nomor_bulan== 5):
    print("ramadhan")
elif (nomor_tanggal >= 2 and nomor_bulan == 5):
    print("syawal")
elif (nomor_tanggal >= 1<=29 and nomor_bulan == 6) :
    print("dzulqaidah")
elif (nomor_tanggal >= 30 and nomor_bulan == 6) or (nomor_tanggal<=29 and nomor_bulan== 7):
    print("dzulhidjah")
elif (nomor_tanggal >= 30 and nomor_bulan == 6) or (nomor_tanggal<=29 and nomor_bulan== 7):
    print("muharam")
elif (nomor_tanggal >= 30 and nomor_bulan == 6) or (nomor_tanggal<=29 and nomor_bulan== 7):
    print("shafar")
elif (nomor_tanggal >= 30 and nomor_bulan == 6) or (nomor_tanggal<=29 and nomor_bulan== 7):
    print("rabiul awal")
elif (nomor_tanggal >= 30 and nomor_bulan == 6) or (nomor_tanggal<=29 and nomor_bulan== 7):
    print("rabiul akhir")
elif (nomor_tanggal >= 30 and nomor_bulan == 6) or (nomor_tanggal<=29 and nomor_bulan== 7):
    print("jumadil ula")
elif (nomor_tanggal >= 30 and nomor_bulan == 6) or (nomor_tanggal<=29 and nomor_bulan== 7):
    print("djumadil akhirah")







    