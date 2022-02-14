import math
with open('sygnaly.txt','r') as plik:
    wiersze = plik.read().splitlines()
    odpowiedz =''
    for i in range(39,len(wiersze),40):
        odpowiedz += wiersze[i][9]
    with open('wyniki4.txt', 'w')as plik2:
        plik2.write('Zadanie 4.1\n\n\n')
        plik2.write(odpowiedz)
        plik2.write('\n\n\n\n')


with open("sygnaly.txt") as file:
    lista = file.read().splitlines()

maxi = 0
odpowiedz =''
for w in lista:
    if len(set(w)) > maxi:
        maxi = len(set(w))
        odpowiedz = f'{w} - {maxi}\n'
with open('wyniki4.txt', 'a')as plik2:
    plik2.write('Zadanie 4.2\n\n\n')
    plik2.write(odpowiedz)
    plik2.write('\n\n\n\n')

with open('sygnaly.txt','r') as plik:
    wiersze = plik.read().splitlines()
    odpowiedz = ''
    slowoJestOk = True
    for w in wiersze:
        for j in range(len(w)-1):
            for i in range(len(w)-1):
                if math.fabs(ord(w[j]) - ord(w[i+1])) >= 10:
                    slowoJestOk = False
                    break
        if slowoJestOk:
            odpowiedz += f'{w}\n'
        slowoJestOk = True
    with open('wyniki4.txt', 'a')as plik2:
        plik2.write('Zadanie 4.3\n\n\n')
        plik2.write(odpowiedz)