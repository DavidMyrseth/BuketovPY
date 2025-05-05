productsPrices = []

while True:
    try:
        name, price = input("Sisesta toote nimi ja hind").split(" ")
        product = {name: price}
        productsPrices.append(product)
    except:
        break


print("Ostetud tooted")
for elem in productsPrices:
    for key, val in elem.items():
        print(key, val)

print("Kogusmma: ", total1)
