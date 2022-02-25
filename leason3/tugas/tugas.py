from numpy import delete


dc1 = {
    'nama' : 'pradita',
    'alamat': 'mataram',
    'umur': 19,
    'kuliah': {
        'universitas' : 'unram',
    },
    'nim':83
}

value = 'universitas mataram'
key = 'universitas'
dc1['kuliah'][key]= value
print(f"data baru {dc1}")
barang = []
dc2={
    'kode': 10,
    'nama': 'pepsoden',
    'harga': 30000
}
dc21={
    'kode': 11,
    'nama': 'axe',
    'harga': 20000
}
barang.append(dc2)
barang.append(dc21)
print(barang)

dc3={
    'kode': [1,2,3],
    'nama': ['sampo','sabun','sapu'],
    'harga': [10000,15000,25000]
}
dc3['kode'].append(4)
dc3['nama'].append('handyplas')
dc3['harga'].append(50000)
print(dc3)

dc3['kode'].remove(3)
dc3['nama'].remove('sapu')
dc3['harga'].remove(25000)
print(dc3)



print(dc3)
