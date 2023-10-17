brukere = {"olan": 0 , "karin": 0}

def lagBrukernavn(mittNavn):
    navn = mittNavn.lower().split()

    brukernavn = navn[0] + navn[1][0]

    i = 1
    while brukernavn in brukere.keys():
        brukernavn = brukernavn + navn[1][i]
        i += 1
    
    brukere[brukernavn] = "ifi.uio.no"

    return brukernavn

print(lagBrukernavn("Aslak Björnerstedt"))
print(lagBrukernavn("Ola Nordstrand"))
print(lagBrukernavn("Ola Nordstrand"))


def lagEpost(brukernavn, suffix):
    return brukernavn + "@" + suffix

print(lagEpost(lagBrukernavn("Bjørn Bjørnsson"), "ifi.uio.no"))


def skrivUtEposter(minOrdbok): 
    for el in minOrdbok:
        print(lagEpost(el, minOrdbok[el]))

ordbok = {"olan": "ifi.uio.no", "karin": "student.matnat.uio.no"}
skrivUtEposter(ordbok)


ordbok2 = {}
bokstav = ""

while bokstav != "s":
    bokstav = input("Skriv inn 'i' for å lage en ny epost, 'p' for å skrive ut epostene og 's' for å avslutte programmet: ")

    if bokstav == "s":
        continue

    elif bokstav == "i":
        navn = input("Skriv inn et navn: ")
        suffix = input("Skriv in en e-post suffix: ")

        brukernavn = lagBrukernavn(navn)
        ordbok2[brukernavn] = suffix

    elif bokstav == "p":
        skrivUtEposter(ordbok2)
    
    else:
        print("Du ga ikke gyldig input.")

