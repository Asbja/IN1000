def antallBokstaver(mittOrd):
    return len(mittOrd)

ord = input("Skriv inn et ord: ")

print(antallBokstaver(ord))

def unikeOrd(minSetning):
    ordbok = {}

    for el in minSetning:
        if el not in ordbok.keys():
            ordbok[el] = 0

        if el in ordbok.keys():
            ordbok[el] += 1

    return ordbok


setning = input("Skriv en setning: ").split()
print(unikeOrd(setning))

setning2 = input("Skriv en setning: ").lower().split()

print(f"Det er {len(setning2)} ord i setningen din.")

dict = unikeOrd(setning2)

# "el" vil være lik en av de unike ordene i setningen siden vi looper gjennom nøkkelverdiene i ordboken, dict[el] vil være antallet ganger 
# ordet forekommer og "antallbokstaver(el)" vil være lengden på ordet siden "antallbokstaver()" funksjonen returnerer lengden på ordet du putter inn.
for el in dict:
    print(f"Ordet '{el}' forekommer {dict[el]} ganger, og har {antallBokstaver(el)} bokstaver i seg.")

#Kunne ha brukt "if-statements" for å gjøre bøyningen av "ganger" og "bokstaver" riktig hvis et ord forekommer 1 gang eller er 1 bokstav
#langt, men det ville gjort koden veldig mye større og styggere uten å oppnå så mye imo

