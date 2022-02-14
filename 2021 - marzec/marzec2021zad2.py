
with open("galerie_przyklad.txt",'r') as plik:
    wszystkieLinie = plik.readlines()
    galerie = {}
    galerie_ilosc = {}
    for w in wszystkieLinie:
        info = w.split(' ')
        galerie[info[1]] = 0
        galerie_ilosc[info[1]] = 0
        for i in range(2,len(info)-1,2):
            galerie[info[1]] += int(info[i]) * int(info[i+1])
            if(info[i] != '0' or info[i]!='0'):
                galerie_ilosc[info[1]] += 1

with open("galerie_przyklad.txt",'r') as plik:
    wszystkieLinie = plik.readlines()
    maxRonzychLokali = 0
    maxRoznychLokaliMiasto = ''
    minRoznychLokali = 9999
    minRoznychLokaliMiasto = 0
    rozneLokale=set()
    for w in wszystkieLinie:
        info = w.split(" ")
        miasto = info[1]
        for i in range(2, len(info) - 1, 2):
            if info[i] != '0' or info[i] != '0':
                powierzchniaLokalu = int(info[i]) * int(info[i+1])
                rozneLokale.add(powierzchniaLokalu)
        if len(rozneLokale) > maxRonzychLokali:
            maxRonzychLokali = len(rozneLokale)
            maxRoznychLokaliMiasto = miasto
        if len(rozneLokale) < minRoznychLokali:
            minRoznychLokali = len(rozneLokale)
            minRoznychLokaliMiasto = miasto


    print(maxRonzychLokali,maxRoznychLokaliMiasto)
    print(minRoznychLokali,minRoznychLokaliMiasto)

