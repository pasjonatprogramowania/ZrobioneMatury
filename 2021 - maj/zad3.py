from collections import Counter
def ktoraLiteraJestNajczesciejDopisywana(instrukcje):
    dopisywaneLitery = []
    for instrukcja in instrukcje:
        instrukcja = instrukcja.rsplit()
        polecenie = instrukcja[0]
        litera = instrukcja[1]
        if polecenie == 'DOPISZ':
            dopisywaneLitery.append(litera)
    return Counter(dopisywaneLitery)

with open("instrukcje.txt",'r') as plik:
    wiersze = plik.readlines()
    print(ktoraLiteraJestNajczesciejDopisywana(wiersze))
