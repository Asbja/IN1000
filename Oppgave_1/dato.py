#Lager variabler får måneden og dagen til de to datoene som får verdien brukeren skriver inn
dato1måned = input("Skriv inn dagen til dato1\n")
dato1dag = input("Skriv inn måneden til dato1\n")
dato2måned = input("Skriv inn dagen til dato2\n")
dato2dag = input("Skriv inn måneden til dato2\n")

#Hvis måneden til dato1 er mindre en måneden til dato2 kommer dato1 garantert før
if (dato1måned < dato2måned):
    print("Riktig rekkefølge!")
#Hvis månedene er like må man sjekke om dagene er større mindre eller like
elif (dato1måned == dato2måned):
    if (dato1dag < dato2dag):
        print("Riktig rekkefølge!")
    elif (dato1dag == dato2dag):
        print("Samme dato!")
#Hvis dagen til dato1 ikke er mindre eller lik dagen til dato2, så kommer dato2 før dato1 og rekkefølgen er feil
    else:
        print("Feil rekkefølge!")
#Hvis måneden til dato1 ikke er mindre eller lik måneden til dato2, så kommer dato2 før dato1 og rekkefølgen er feil
else:
    print("Feil rekkefølge!")