
dc1 = {
    'nama' : 'pradita',
    'alamat': 'mataram',
    'umur': 19,
    'kuliah': {
        'universitas' : 'unram',
    },
    'nim':83
}
print(dc1)
'mengakses'
print(dc1["nama"])
print(dc1['kuliah']['universitas'])

'mengubah umur'
value = 20
key = 'umur'
dc1[key]=value
print(f"data baru {dc1}\n")
#menghapus data dengan method pop
hapus = "nim"
dc1.pop(hapus)
print(f'hapus nim : {dc1}')
