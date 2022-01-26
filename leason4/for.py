games = ["dota","valorant", "csgo"]
print("perulangan")

for i in games:
    print(i)

print("break")
for a in games:
    if a == "csgo":
        break
print("continue")
for b in games:
    if b == "valorant":
        continue
    else:
        print (b)
print("range")
for c in range (10):
    print(c)
print("range 10 sampai 50")
for c in range (10,50):
    print (c)
print("range 10 - 50 dengan selisih 2")
for d in range (10,50,2):
    print(d)


