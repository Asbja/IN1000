# Oppretter en variabel 'i' og sett den til 1.
i = 1

# Oppretter en tom liste 'talliste'.
talliste = []

# Oppretter en variabel 'minSum' og sett den til 0. Denne vil bli brukt til å telle antall elementer i 'talliste'.
minSum = 0

# Bruker en while-løkke som fortsetter å kjøre så lenge 'i' ikke er lik 0.
while i != 0:
    # Ber brukeren om å skrive inn et positivt tall og lagre svaret i 'i'.
    i = int(input("Skriv inn et positivt tall: "))
    
    # Legger verdien av 'i' til 'talliste'.
    talliste.append(i)
    
    # Øker 'minSum' med 1 for å telle antall elementer i 'talliste'.
    minSum += 1

# Skriver ut alle elementene i 'talliste' ved å iterere gjennom listen.
for i in talliste:
    print(i)
    # Øker 'minSum' med 1 i hver iterasjon.

# Skriver ut totalt antall elementer i 'talliste' (lengden av listen).
print(minSum)

# Oppretter en variabel 'minmax' og sett den til det første elementet i 'talliste'.
minmax = talliste[0]

# Finner det minste elementet i 'talliste' ved å sammenligne hvert element med 'minmax'.
for el in talliste:
    if el < minmax:
        minmax = el

# Finner det største elementet i 'talliste' ved å sammenligne hvert element med 'minmax'.
for el in talliste:
    if el > minmax:
        minmax = el