#En quiz der svarene til brukeren blir lagret i enn liste også sammenlignet med fasitsvarene som ligger i en annen liste

#Lagerer fasitsvar i en liste, lagrer tom liste som skal inneholde brukerens svar og setter poeng til 0
fasit = [11, "Berlin", "Russland"]
svar = []
poeng = 0

#Stiller brukeren et spørsmål, gjør svaret om til en integer, lagrer det i en variabel og appender variabelen til "svar" listen
svar1 = int(input("Hvor mange fylker er det i Norge? 11/19/15\n")) 
svar.append(svar1)

#Stiller brukeren et spørsmål, lagrer svaret i en variabel og appender variabelen til "svar" listen
svar2 = input("Hva er hovedstaden i Tyskland? Hamburg/Berlin/München\n")
svar.append(svar2)

svar3 = input("Hva er det største landet i verden? Kina/USA/Russland\n")
svar.append(svar3)

#Looper gjennom elementene i "svar"-listen, sjekker om individuelle svar matcher et element i fasiten, hvis det gjør legges 1 til verdien til poeng
for el in svar:
    if el in fasit:
        poeng += 1

#Sjekker om poeng er lik 0 eller mindre enn 3, hvis de sjekkene ikke er True må poeng=3, forskjellige meldinger printes avhengig av poengsummen til brukeren
if poeng == 0:
    print("Du svarte feil på alle spørsmålene")
elif poeng < 3:
    print("Du fikk noen feil og noen riktige.")
else:
    print("Gratulerer, du fikk alt riktig!")