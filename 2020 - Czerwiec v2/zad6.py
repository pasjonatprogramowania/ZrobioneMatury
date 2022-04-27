# def szyfryj(w,k):
#     odpowiedz= ''
#     w = w.upper().replace(" ","")
#     for i in w:
#         odpowiedz += chr((ord(i)+k-65)%26+65)
#     return odpowiedz
# def deszyfruj(w,k):
#     k *= -1
#     return  szyfryj(w,k)
# with open('dane_6_1.txt','r') as plik:
#     wiersze = plik.read().splitlines()
#     k =107
#     odpowiedz = ''
#     for wiersz in wiersze:
#         odpowiedz += f"""{szyfryj(wiersz,k)} \n"""
#     with open("wynik_6_1.txt","w") as plik2:
#         plik2.write("wynik 1\n\n\n")
#         plik2.write(odpowiedz)
#         plik2.write('\n\n\n')
#
# with open('dane_6_2.txt','r') as plik:
#     wiersze = plik.read().splitlines()
#     odpowiedz =''
#     for wiersz in wiersze:
#         wiersz = wiersz.rsplit()
#         w = wiersz[0]
#         k = int(wiersz[1])
#         odpowiedz += deszyfruj(w, k)
#     print(odpowiedz)
