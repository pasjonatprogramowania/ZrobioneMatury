import random

"""zad1"""
tablica = []
for i in range(175):
    tablica.append(random.randint(0,150))
tablica.sort()
liczymy = 1
odpowiedz = ''
for i in range(len(tablica)-1):
    a = tablica[i]
    b = tablica[i+1]
    if  a==b:
        liczymy+=1
    else:
        if liczymy > 3:
            odpowiedz+=f"{tablica[i]} byla {liczymy} razy\n"
            liczymy = 1
print(f"Zad1 - {odpowiedz}")
"""zad2"""
import statistics
# print(statistics.median(tablica))
def mediana(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j + 1], lista[j] = lista[j], lista[j + 1]

    if len(lista) % 2 == 0:
        mediana = lista[int(len(lista) / 2)] + lista[int(len(lista) / 2 - 1)]
        mediana /= 2
    else:
        mediana = lista[int(len(lista) / 2)]
    return mediana
print(f"Zad2 - {mediana(tablica)}")
"""zad3"""
tablica2 = []
for i in range(70):
    tablica2.append(random.randint(0,500))
min = min(tablica2)
max = max(tablica2)
minl = 1
maxl = 1
for i in range(len(tablica2)-1):
    a = tablica2[i]
    if a == min:
        minl+=1
    if a == max:
        maxl+=1
print(f"Zad3 - {min} byla {minl}\n{max} byla {maxl}\n")
"""zad4"""
w = input("podaj liczbe: ")
try:
    print(f"Zad4 - Liczba znajduje sie na pozycji: {tablica2.index(w)}")
except:
    print("Zad4 - nie ma takiej liczby")
"""zad5"""
a = "Grzegorz Oparcik"
tab = list(a)

for i in range(len(tab)):
    mini = i
    for j in range(i+1, len(tab)):
        if tab[mini] > tab[j]:
            mini = j
    tab[i], tab[mini] = tab[mini], tab[i]
print("Zad5 -",''.join(tab))