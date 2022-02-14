with open("przyklad.txt",'r') as plik:
    wiersze = plik.readlines()
def wykonajPolecenie(instrukcje):
    napis = ""
    for instrukcja in instrukcje:
        instrukcja = instrukcja.rsplit()
        polecenie = instrukcja[0]
        wartosc = instrukcja[1]
        if polecenie  == "DOPISZ":
            napis +=wartosc
        if polecenie == "ZMIEN":
            napis = list(napis)
            napis[len(napis)-1] = wartosc
            napis = ''.join(napis)
        if polecenie == "USUN":
            napis = list(napis)
            napis[len(napis)-1] = ''
            napis = ''.join(napis)
        if polecenie == "PRZESUN":
            index_l = napis.index(wartosc)
            ascii_l = ord(wartosc)+1
            if ascii_l>90:
                ascii_l -= 26
            napis = list(napis)
            napis[index_l] = chr(ascii_l)
            napis = ''.join(napis)
    return napis

print(wykonajPolecenie(wiersze))
