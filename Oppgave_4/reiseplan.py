# Oppretter tre tomme lister: 'steder', 'klesplagg', og 'avreisedatoer'.
steder = []
klesplagg = []
avreisedatoer = []

# Bruker en for-løkke til å be brukeren om å legge til reisemål, klesplagg og avreisedatoer.
for i in range(5):
    steder.append(input("Skriv inn et reisemål: "))
    klesplagg.append(input("Skriv inn et klesplagg: "))
    avreisedatoer.append(input("Skriv inn en avreisedato: "))

# Oppretter en tom liste 'reiseplan' og legger 'steder', 'klesplagg' og 'avreisedatoer' i denne listen som underlister.
reiseplan = []
reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedatoer)

# Skriver ut hele reiseplanen ved å iterere gjennom elementene i 'reiseplan'.
for el in reiseplan:
    print(el)

# Ber brukeren om å angi en posisjon i 'reiseplan' og en posisjon i 'steder', 'klesplagg' eller 'avreisedatoer'.
pos1 = int(input("Skriv en posisjon i reiseplan: "))
pos2 = int(input("Skriv en posisjon i steder, klesplagg eller avreisedatoer: "))

# Sjekker om de angitte posisjonene er gyldige indekser i 'reiseplan'.
if (pos1 >= 0 and pos1 < 3) and (pos2 >= 0 and pos2 < 5):
    # Hvis posisjonene er gyldige, skriv ut elementet i 'reiseplan' på de angitte posisjonene.
    print(reiseplan[pos1][pos2])
else:
    # Hvis posisjonene er ugyldige, gi beskjed om det.
    print("Ugyldig input!")
    