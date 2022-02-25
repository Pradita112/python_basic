def fullname(**call):
    print(call)
    print(f"saya lahir pada tanggal {call['tanggal']} dan lahir bulan {call['bulan']}")


fullname(tanggal="08",bulan="mei")

def fullname(**calls):
    print(calls)
    print(f"nama saya adalah{calls['nama']} hobi saya adalah  {calls['hobi']}")


fullname(nama="budi ",hobi="bermain game")


