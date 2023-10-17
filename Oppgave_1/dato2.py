#Ber brukeren om å legge in datoen som et heltall med måneden først for å gjøre det lett å sammenligne datoene
#gjør svaret om til et heltall med int() metoden
dato1 = int(input("Skriv inn dato som et heltall, f.eks 5.April blir 405.\n"))
dato2 = int(input("Skriv inn dato som et heltall, f.eks 15.April blir 415.\n"))

#Sjekker om dato en kommer før, eller er lik dato2
if (dato1 < dato2):
    print("Riktig Rekkefølge!")
elif (dato1 == dato2):
    print("Samme dato!")
#Hvis dato1 ikke er mindre eller lik dato2 er den større, og datoene er dermed i feil rekkefølge
else:
    print("Feil rekkefølge!")

