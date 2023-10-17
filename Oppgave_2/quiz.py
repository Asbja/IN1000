#En quiz med 3 spørsmål, der brukeren blir gitt tre svarsalternativer per spørsmål, hvis de svarer riktig får de 1 poeng
#Etter at de har svart på det siste spørsmålet får de forskjellige tilbakemeldinger avhengig av hvor mange poeng de fikk

#Setter poeng til 0 og stiller første spørsmål med en input, lagrer svaret i variabelen svar1.
poeng = 0
svar1 = input("Hva er navnet på det høyeste fjellet i Norge? Galdhøpiggen/Glittertinden/Skagastøltind\n")

#Sjekker om svar1 == Galdhøpiggen, hvis det er printes meldingen "Riktig svar!" poengsummen økes med 1
if svar1 == "Galdhøpiggen":
    print("Riktig svar!")
    poeng += 1
else:
    print("Feil svar!")

#Gjør det samme som med svar1, men stiller et annet spørsmål og sjekker for et annet svar
svar2 = input("Hva er den nest største byen i Norge? Stavanger/Bergen/Trondheim\n")
if svar2 == "Bergen":
    print("Riktig svar!")
    poeng += 1
else:
    print("Feil svar!")

svar3 = input("Hva er hovedstaden til Norge? Oslo/Trondheim/Bergen\n")
if svar3 == "Oslo":
    print("Riktig svar!")
    poeng += 1
else:
    print("Feil svar!")

#Setter opp en if-sjekk som printer forskjellige tilbakemeldinger til brukeren avhengig av hvor mange poeng de fikk
if poeng == 0:
    print("Du svarte desverre feil på alle spørsmålene.")
elif poeng < 3:
    print("Du fikk noen feil og noen riktig.")
else:
    print("Gratulerer! Du svarte riktig på alle spørsmålene og fikk 3/3 poeng!")