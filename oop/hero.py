from xml.dom.minidom import DocumentFragment


class hero():

    def __init__(self,name,hp,damage,armor):
        self.name= name
        self.damage = damage
        self.hp = hp
        self.armor = armor

    def status(self):
        print(f"{self.name} memiliki hp {self.hp},damage {self.damage}, dan armor {self.armor}")

    def attack(self,enemy):
        print(f"{self.name} menyerang {enemy.name} denagn damage {self.damage}")
    
    def difussal(self):
        self.damage+= 50
        print(f"damage hero {self.name} bertambah 50 poin")

h1 = hero('juggernaut',2000,200,20)
h2 = hero('medusa',2100,100,22)
h1.status()
h2.attack(h1)
h1.attack(h2)
h1.difussal()
h1.status()




    

