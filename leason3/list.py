"List [ ]"

campuran = [True, False, "Adit", 12, 9.8,[1,2,3,"Kopi Manis"], "Bakso"]
print(f"Data campuran : {campuran}")
print(f"Tipe datanya adalah : {type(campuran)}")
games = ["Dota", "Vaoran", "CS GO", "Basara", "Harvest Moon", "Mario Bros"]
#Mengakses data berdasarkan index
print(f"Game pada index 3 : {games[3]}")
print("game pada index 2",campuran[5][2]) #list di dalam list

#Mengakses data paling akhir dengan negative index
print(f"Game dengan index paling akhir adalah : {games[-1]}")


#Mengakses data pada range tertentu
print(f"Data pada index 3 sampai 5 {games[3:6]}")
print(f"data pada index pertama sampai 5 {games[:6]}")
#Menambah data dengan menggunakan method append()
print(f"Koleksi game lama : {games}")
games.append("FIFA")
print(f"Koleksi game terbaru : {games}")

#menambah data menggunakan method insert
games.insert(3, "PES")
print(f"Koleksi game baru {games}")
#menambahkan dengan extend
games.extend(campuran)
print (f"extend data : {games}")
print("cara lainnya ",games + campuran)
print()
#Mengetahui index dari sebuah data yang ada dalam sebuah list
print(games.index("CS GO"))
#looping list
#for i in games:
 #   print(i)"


 #mengubah data
print(games)
games[2]= "NFS"
print (f"ganti games {games}")

#menghapus list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#sort
listt =[1123,2312,12,32,532]
listt.sort()
print(listt)



