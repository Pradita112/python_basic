def luas_volume(p,l,t):
    hasil = p*l*t
    return hasil
a = luas_volume(5,6,7)
print(f"luas balok adalah {a}")

def volume_limas(la,t):
    hasil = 1/2*la*t
    return hasil

b = volume_limas(20,10)
print(f"volume limas adalah : {b}")

def volume_bola(r):
    hasil = 4/3 * 22/7 *r*r*r
    return hasil
c = volume_bola(20)
print(f"volume bola adalah : {c}")