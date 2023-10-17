#Ber brukeren om å svare på spørsmålet ved å skrive inn ja eller nei. 
svar = input("Har du lyst på en brus? ja/nei\n")

#Setter opp en if-statment som printer "Her har du en brus!" hvis brukeren skrev ja og "Den er grei." hvis brukeren skrev nei.
if (svar == "ja"):
    print("Her har du en brus!")
elif (svar == "nei"):
    print("Den er grei.")
#Å Sjekke hva brukeren svarte, hvis de ikke svarte ja/nei er unødvendig fordi da skulle programmet uansett svare:"Det forstod jeg ikke helt"
else:
    print("Det forstod jeg ikke helt.")