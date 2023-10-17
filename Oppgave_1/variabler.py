#Bruker en input for å be brukeren om en string som jeg legger i variabelen navn, skriver ut "Hei" også stringen brukeren skrev inn.
navn = input("Hva heter du?\n")
print(f"Hei {navn}!")

#Lager to varibaler med to forskjellige tallverdier, lager en tredje variabel som har verdien til tall1 - tall2 som sin verdi,
#Dette blir differansen mellom de to verdiene, skriver ut "Differanse:" også den tredje verdien
tall1 = 5
tall2 = 4
differanse = tall1 - tall2
print(f"Differanse: {differanse}")

#Ber om en ny string fra brukeren, lager en ny variabel som kombinerer de to tidligere stringene vi har fått fra brukeren
navn2 = input("Oppgi et nytt navn.\n")
sammen = navn + navn2
print(sammen)

#Endrer "sammen" variabelen så den skrives ut som med et og igjen de to stringene som brukeren har lagt inn
sammen = f"{navn} og {navn2}"
print(sammen)