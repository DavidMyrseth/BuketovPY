productsPrices = []

def sisesta_toode():
    while True:
        sisend = input("sisesta nimi, hind, kogus")
        if not sisend:
            break
        try:
            name, price = input("Sisesta toote nimi ja hind").split(" ")
            hind = float(hind)
            kogus = int(kogus)
            for elem in ostukorv:
                if elem["nimi"] == nimi:
                    elem["kogus"] += kogus
                    break
            else:
                ostukorv.append({
                    "nimi":nimi,
                    "hind":hind,
                    "kogus":kogus,
                })
                print(ostukorv)
        except ValueError:
            print("sisesta nimi, hind, kogus")

def arvuta_kogusumma():
    summa = 0
    for elem in ostukorv:
        summa += elem["hind"]*elem["kogus"]
    return summa

def kuva_arve():
    print("ostutseki")
    print("-"*50)
    for elem in ostukorv:
        for nimi, andmed in elem.items():



kuva_arve()


            # print("nimi", nimi)
            # print("hind", andmed[0]),
            # print("kogus", andmed[1])
        

# CTRL K C

# def arvuta_kogusumma():
#     pass
# def kuva_arve():
#     pass


# print("Ostetud tooted")
# for elem in productsPrices:
#     for key, val in elem.items():
#         print(key, val)

# print("Kogusmma: ", total1)
