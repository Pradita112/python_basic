class student():    
    def __init__(self, id, nim, first_name, last_name, courses):
        self.id = id
        self.nim = nim
        self.fn = first_name
        self.ln = last_name
        self.cs = courses

    def __repr__(self):
        return self.fn + " " + self.ln

    def description(self):

        print(f"{self.nim} -- {self.fn} -- {self.cs}")

class course():
    def __init__(self,name:str, lecture:str):
        self.name = name
        self.lecture = lecture

    def __repr__(self):
        return self.name

c1 = course("analisis algo","budi setiawan")
s1 = student(1,123,"adit","pradita",c1.name)
s1.description()
del(c1)
s1.description()    

