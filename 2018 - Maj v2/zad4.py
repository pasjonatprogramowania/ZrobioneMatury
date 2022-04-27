plik = open('przyklad.txt','r')

wiersze = plik.read().splitlines()
for wiersz in range(0,len(wiersze)-1,40):
    for litera in range(0,len(wiersz),10):
        print(l)

