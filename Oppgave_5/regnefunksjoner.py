def addisjon(num1, num2):
    return num1 + num2

print(addisjon(4, 7))

def subtraksjon(num1, num2):
    return num1 - num2

def divisjon(num1, num2):
    return num1 / num2

assert subtraksjon(8, 5) == 3
assert subtraksjon(-9, -2) == -7
assert subtraksjon(7, -6) == 13

assert divisjon(6, 3) == 2
assert divisjon(-8, -2) == 4
assert divisjon(14, -7) == -2

def tommerTilCm(antallTommer):
    assert antallTommer != 0
    return antallTommer * 2.54

print(tommerTilCm(5))

def skrivBeregninger():
    print("Utregninger: ")
    tall1 = float(input("Skriv inn tall 1: "))
    tall2 = float(input("Skriv inn tall 2: "))

    print(f"Resultatet av summering: {addisjon(tall1, tall2)}")
    print(f"Resultatet av subtraksjon: {subtraksjon(tall1, tall2)}")
    print(f"Resultatet av divisjon: {divisjon(tall1, tall2)}")
    
    print("Konvertering fra tommer til cm:")
    tall3 = float(input("Skriv inn en tall: "))
    print(f"Resultat: {tommerTilCm(tall3)}")

skrivBeregninger()