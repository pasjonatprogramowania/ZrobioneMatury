# with open("przyklad.txt",'r') as plik:
#     wiersze = plik.readlines()
#     ileLiczb =0
#     for wiersz in wiersze:
#         for w in wiersz:
#             if w == '1' or w == '2' or w == '3'or  w =='4'or  w =='5'or  w =='6'or  w =='7'or w =='8'or  w =='9' or w =='0':
#                 ileLiczb+=1


# with open("przyklad.txt",'r') as plik:
#     wiersze = plik.readlines()
#     wynik = ''
#     for i in range(19,len(wiersze),20):
#         szukanyWiersz=wiersze[i]
#         wynik += szukanyWiersz[int(i/20)]
#
#     print(wynik)

# with open("przyklad.txt",'r') as plik:
#     wiersze = plik.readlines()
#     napis = ''
#     polindrom = ''
#     for wiersz in wiersze:
#         w = wiersz.strip()
#         napis = f'{w[len(w) - 1]}{w}'
#         if napis == napis[::-1]:
#             polindrom = f'{napis[(len(napis)-1)//2:(len(napis)+2)//2]}'
#     print(polindrom)

with open("przyklad.txt",'r') as plik:
    wiersze = plik.readlines()
    for wiersz in wiersze:
        w = wiersz.strip()
        wartosc = ''
        for i in range(0,len(w)-1,2):
            if w[i] in '1234567890' and w[i+2] in '1234567890':
                napis = w[i] + w[i+2]
                if 65 < int(napis) < 90:
                    wartosc += chr(int(napis))
        print(wartosc)


