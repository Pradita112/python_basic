class build():
    room = []
    def __init__(self,id,name,color):
        self.id = id
        self.name = name
        self.color = color

    def description(self):
        print(f"bangunan ke {self.id}; nama : {self.name}; warna banguan : {self.color}; memiliki ruanagan {self.room}")
    def add_room(self,r):
        self.room.append(r)

class room():
    def __init__(self,name:str):
        self.name = name
        print(f"ruangan {self.name}berhasil di buat")
    
    def __repr__(self):
        return self.name
    
b1 = build(1,"ITEC Smart","creem")
r1= room("instagram")

b1.description()
b1.add_room(r1)
b1.description()