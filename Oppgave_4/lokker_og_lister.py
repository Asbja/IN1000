# Oppretter en variabel 'i' og setter den til 0.
i = 0

# Oppretter en tom liste 'talliste'.
talliste = []

# Bruker en while-løkke for å legge til tallene 0 til 9 i 'talliste'.
while i < 10:
    talliste.append(i)
    i += 1  # Øker 'i' med 1 i hver iterasjon.

# Oppretter en ny tom liste 'talliste2'.

talliste2 = []

# Bruker en for-løkke for å legge til tallene 0 til 9 i 'talliste2'.
for i in range(10):
    talliste2.append(i)

# På linje 16 lager jeg en saminlg gjennom metoden range()
# Samlingen inneholder tallene 0-9

# Oppretter en tom liste 'mine_tall'.
mine_tall = []

# Tilordner 'i' til 0.
i = 0

# Bruker en while-løkke for å legge til tallene mellom 0 og 20 i mine_tall i intervaller av 3
while i < 20:
    mine_tall.append(i)
    i += 3  # Øk 'i' med 3 i hver iterasjon.

# Skriver ut alle elementene i 'mine_tall' ved å iterere gjennom listen.
for tall in mine_tall:
    print(tall)

# Skriver ut indeksene til elementene i 'mine_tall' ved å bruke en for-løkke.
for i in range(len(mine_tall)):
    print(i)

# Multipliserer hvert element i 'mine_tall' med 10 ved å bruke en for-løkke.
for i in range(len(mine_tall)):
    mine_tall[i] = mine_tall[i] * 10

# Skriver ut den oppdaterte listen 'mine_tall'.
print(mine_tall)

#Det fungerer bare når du kaller en indeks fra listen fordi at når du looper gjennom elementene i listen ser du bare på en kopi av et
#element i listen, ikke selve elementet. Å gange kopien av elementet i listen med 10 endrer ikke selve listen, du må kalle på elementer
#i listen med indeksen for å kunne endre selve listen.

#Listen forblir uendret etter at du kjører for-loopen.

