#Lager en ordbok der nøkkelverdiene er navn og innholdsverdiene er matplanen til et individ
personer = {"Kari Nordmann": ["brød", "egg", "pølser"], 
            "Aslak Jo": ["frokostblanding", "omelett", "pizza"],
            "Bjørn Bo": ["yoghurt", "nudler", "ramen"]}

#Definerer funksjonen
def matplan():
    #Bruker keys() metoden for å få nøkkelverdiene i "personer" og bruker så list() for å sette navnene inn i en liste som jeg kan printe.
    print(f"Dette er navnene til beboerne på sykehjemmet: {list(personer.keys())}")
    #Ber brukeren om å skrive inn et av navnene, sjekkor om det brukeren skrev inn er en nøkkelverdi i "personer"
    beboer = input("Skriv inn navnet til en av beboerne: ")
    #Hvis det er, skrives matplanen til personen som brukeren skrev inn ut, ellers printes meldingen: "Denne personen er ikke registrert i sykehjemmet."
    if beboer in personer:
        print(f"Matplanen til {beboer}: {personer[beboer]}")
    else:
        print("Denne personen er ikke regirstret i sykehjemmet.")

#Kaller funksjonen
matplan()

#3a Brukernavnene til alle IFI studentene burde lagres i en mengde fordi den tillater ikke like verdier. 
# Alle brukernavn burde være forskjellige og en mengde sikrer at de er det.
# Siden mengder ikke er indeksert er det også mye raskere å sjekke om et brukernavn finnes i mengden eller ikke,
# sammenlignet med hvis du lagret brukernavnene i en liste eller ordbok.

#3b Brukernavn og antall poeng burde lagres i en ordbok der brukernavnet er nøkkelverdien og poengsummet er innholdsverdien. 
# Dette gjør det enkelt å finne ut hvor mange poeng en person fikk og sammenligne poengsummene til personer.

#3c Siden bare navn skal lagres ville en liste fungert best. En mengde fungerer ikke siden to personer kan ha samme navn.

#3d En liste eller mengde som inneholder all maten gjestene er allergisk mot. 
#Gir tydelig oversikt over hva som kan og ikke kan være i menyen.

