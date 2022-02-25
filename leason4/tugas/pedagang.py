keranjang= []
rincian= []
tomat = "tomat"
ayam = "ayam"
kol = "kol"
bumbu_dapur= "bumbu_dapur"
bayam = "bayam"
tambahan = "iya"
while tambahan == "iya":
    print("list dagangan ")
    print("1. tomat")
    print("2. kol")
    print("3. ayam")
    print("4. bayam")
    print("5. bumbu_dapur")
    belanja=input ("ingin membeli yang mana : ")
    if belanja == tomat:
        rincian.append()
        keranjang.append(belanja)
    elif belanja == kol:
        rincian.append(7000)
        keranjang.append(belanja)
    elif belanja == ayam:
        rincian.append(25000)
        keranjang.append(belanja)
    elif belanja == bayam:
        rincian.append(2000)
        keranjang.append(belanja)
    elif belanja == bumbu_dapur:
        rincian.append(4000)
        keranjang.append(belanja)
    tambahan = input("apakah ada tambahan lain iya atau tidak: ")
print (keranjang)
print(rincian)
print (sum(rincian))