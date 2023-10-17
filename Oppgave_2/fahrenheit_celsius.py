#Definerer far som et heltall gitt av brukeren, definerer variabelen cel som konverterer fahrenheit verdien til celsius gjennom en formel
far = int(input("Skriv inn en temperatur i heltallsform: "))
cel = (far-32) * 5/9
print(cel)