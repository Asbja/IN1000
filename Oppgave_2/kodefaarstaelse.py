#Den første linjen av koden vil kjøre, det vil stå "Tast inn et heltall." i terminalen og brukeren vil kunne inputte noe
#Når brukeren trykker enter vil du få en error-melding fordi du har prøvd å plusse sammen en integer med en string, det er ikke mulig

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")
