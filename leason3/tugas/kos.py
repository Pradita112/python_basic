"dedi rendi juki"

"amel,sinta"

kos_putri = ["amel,sinta"]
kos_putra = ["dedi, rendi, juki"]

nama = (input("masukan nama: "))
jenis_k = (input ("masukan jenis kelamin: "))
ttl= input("masukan tempat dan tanggal lahir : ")

if jenis_k == "pria":
    kos_putra.append(nama)
    print(kos_putra)
elif jenis_k== "wanita":
    kos_putri.append(nama)
    print(kos_putri)

