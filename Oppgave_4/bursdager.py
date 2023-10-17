#Lag en tom ordbok, brukeren skal kunne definere hvor mange personer og deres bursdager de vil legge til.
#Bruk en for loop for å la brukeren legge inn personer og deres bursdager.
#La brukeren hente ut bursdagen til en person gjennom å skrive inn navnet deres.
 
# Oppretter en tom ordbok for å lagre bursdager.
bursdager = {}

# Ber brukeren om hvor mange bursdager de ønsker å lagre og lagrer svaret i variabelen 'antall'.
antall = int(input("Hvor mange bursdager trenger du å lagre? "))

# Looper gjennom antall ganger brukeren har angitt for å legge til bursdager i ordboken.
for el in range(antall):
    # Ber brukeren om å skrive inn navnet til en venn og lagre svaret i variabelen 'navn'.
    navn = input("Skriv inn et navn til en venn: ")
    
    # Ber brukeren om å skrive inn bursdagen til vennen og lagrer svaret i variabelen 'bursdag'.
    bursdag = input("Skriv inn busdagen deres i dette formatet, 15. September: ")
    
    # Legger til bursdagen i ordboken med navnet som nøkkel og bursdagen som verdi.
    bursdager[navn] = bursdag

# Ber brukeren om å skrive inn navnet på personen de ønsker å finne bursdagen til og lagre svaret i variabelen 'person'.
person = input("Skriv inn navnet til personen du trenger bursdagen til: ")

# Skriver ut bursdagen til den angitte personen ved å slå opp nøkkelen (navnet) i ordboken.
print(bursdager[person])






