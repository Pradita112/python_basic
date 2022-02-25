
def tekateki():
    print("-------------------teka teki---------------------")
    print('tekan enter untuk ke petunjuk selanjutnya')
    step1()
    print (" enter untuk petunjuk selanjutnya")
    step2()
    print (" enter untuk menjawab")
    step3()

def step1():
    print("dia merupakan hewan berkaki 4 dan memakan daging")

def step2():
    print("dia merupakan hewan ciri has sumatra")

def step3():
    a=input("masukan jawaban anda : ")

    if a == "harimau" or a == "HARIMAU":
        print("selamat anda benar ")
    else:
        "jawaban anda salah"
tekateki()