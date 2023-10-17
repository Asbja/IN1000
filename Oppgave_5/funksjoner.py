def adder(tall1, tall2):
    return tall1 + tall2

print(adder(3, 5))
print(adder(5, 8))



ord = input("Skriv inn en tekststreng: ")
bokstav = input("Skriv inn en bokstav som finnes i tekststrengen: ")

def tellForekomst(minTekst, minBokstav):
    count = 0
    for i in minTekst:
        if i == minBokstav:
            count += 1

    return count

print(tellForekomst(ord, bokstav))