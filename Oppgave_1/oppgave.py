tall1 = int(input("Skriv tall 1: \n"))
tall2 = int(input("Skriv tall 2: \n"))

if tall1 > tall2:
    minst = tall2
elif tall1 == tall2:
    print("Tallene er like")
else:
    minst = tall1
print(minst)