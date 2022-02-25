#TUPLE
zoo = ('kangguru','singa','bebek','angsa','kuda')
print(f' menyimpan daftar hewan kebun binatang pada tuple : {zoo}')

#mengakses data berdasarkan indeks

print(f'hewan pada indeks 3 : {zoo[3]}')
print(f'hewan pada indeks -3 : {zoo[-3]}\n')
#mengakses  pada range tertentu
print(f'daftar hewan pada range 2- 5 {zoo[2:5]}')
#mengakses item (zoo) dari awal sampai indeks tertentu
print(f'daftar hewan dari awal sampai indeks 3{zoo[:4]}')
#mengakses dari indeks tertentu sampai akhir
print(f'daftar hewan dari indeks 3{zoo[3:]}')
#mengakses negative indeks
print(f'daftar hewan dari indeks -4 sampai -1 {zoo[-4:-1]}\n')
#cek item pada sebuah tuple
tebak = input("tebak hewan: ")
if tebak in zoo:
    print(f"anda benar , hewan {tebak} tersebut ada di zoo : {zoo} \n")
else:
    print("anda salah")

#update tuple
print(f'hewan sebelum update: {zoo}')
new_animal = input('ganti bebek dengan hewan: ')
zoo = list(zoo)
zoo[2]= new_animal
zoo = tuple(zoo)
print(f"new animal : {zoo}")
#ADD item in tuple
'cara 1'
zoo = list(zoo)
zoo.append("gajah")
print(zoo)
'cara 2'
m= ('macan',)
zoo+= m
print(f'tambaha mcan : {zoo}')

#unpack 
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#JOIN TUPPLE
angka =('1','2','3')
huruf = ('a','b','c')
gabung = angka + huruf

print("angka join huruf",gabung)

#menghitung panjang tuple dengan method count
angka2 = (1,2,3,3,4,4,5,5,5,5,5,5,6,6,6,7,7,7,7,7)
print("menghitung banyaknya angka 5",angka2.count(5))