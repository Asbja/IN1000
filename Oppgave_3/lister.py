#Lager en liste som består av 3 integers, printer ut det første og tredje elementet
list = [3, 5, 8]
print(list[0], list[2])

#Lager en tom liste, legger inn fire navn gjennom en input funksjon
tom = []
tom.append(input("Skriv inn et navn: "))
tom.append(input("Skriv inn et navn: "))
tom.append(input("Skriv inn et navn: "))
tom.append(input("Skriv inn et navn: "))

#Sjekker hvis stringen "Aslak" finnes i listen "tom", hvis den gjør printes "Du husket meg!" elles printes "Glemte du meg?"
if "Aslak" in tom:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

#Lager en ny tom liste, og en variabel som jeg setter lik 1
list2 = []
prod = 1
#Bruker sum() methoden for å legge sammen verdiene i "list", appender resultatet i "list2"
list2.append(sum(list))

#Lager en loop som looper gjennom elementene i list, setter "prod" lik "prod" * "i", i vil først være 3 så 5 så 8
for i in list:
    prod *= i
list2.append(prod)

#Legger sammen "list" og "list2" til "list3"
list3 = list + list2
print(list3)

#Fjerner det siste elementet i "list3" to ganger
list3.pop()
list3.pop()
print(list3)
