#Definerer funksjonen pris()
def pris():
    #Setter variabelen "alder" lik et tall brukeren skriver inn, setter "bilettpris til 0"
    alder = int(input("Hvor gammel er du: "))
    bilettpris = 0
    #Sjekker først om alder er mindre eller lik 17, hvis den er settes bilettpris til 30, sjekker så om alder er mindre en 63
    #Hvis den er settes bilettpris til 50, ellers settes bilettpris til 35 
    if alder <= 17:
        bilettpris = 30
    elif alder < 63:
        bilettpris = 50
    else:
        bilettpris = 35
    print(f"Bilett koster: {bilettpris}")

#Kaller prosedyren pris()
pris() 

#Prosedyren fungerer, skriver riktig bilettpris til riktig alder