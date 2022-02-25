class Tumbuhan():
    bagian = []
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def description(self):
        print(f" tumbuhan : {self.name}; berwarna : {self.color}")

    def add(self,o):
        self.bagian.append(o)

class Organ():
    def __init__(self,name:str):
        self.name = name
        print(f"  menambahkan {self.name} ")
    
    def __repr__(self):
        return self.name

p1 = Tumbuhan("mangga","hijau")
p2 = Organ("klorofil")

p1.description()
p1.add(p2)
p1.description()
    
