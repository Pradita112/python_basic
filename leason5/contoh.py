def pelajaran(**univ):
    print(univ)
    print(f"saya mendapatkan {univ['nilai']}dalam mata pelajaran{univ['matkul']}dengan dosen pembimbing {univ['dosen']}")

pelajaran(nilai=80, matkul='matematika',dosen='pak pasek\n')


def funct(*args):
    print(args)
    print(f"saya berasal dari {args[0]} yaitu di {args[1]}")

funct("jawa tengah","boyolali")

    

