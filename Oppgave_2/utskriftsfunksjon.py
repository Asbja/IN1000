#Definerer prosedyre som ber brukeren om navn og bosted, lagrer det i separate variabler
def utskriftsfunksjon():
    navn = input("Skriv inn navn: ")
    bosted = input("Hvor kommer du fra? ")
    #Printer så en respons som bruker verdiene brukeren skrev inn
    print(f"Hei, {navn}! Du er fra {bosted}.")

#Lager en loop som looper gjennom en sekvens av tre tall som blir laget av range-funksjonen, siden sekvensen har 3 elementer kalles prosedyren 3 ganger
for i in range(3):
    utskriftsfunksjon()