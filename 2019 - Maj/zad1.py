# def czyJestPotega(liczba):
#     liczba = int(liczba)
#     if liczba < 0:
#         return False
#     while (liczba > 1):
#         if liczba%3 != 0:
#             return False
#         liczba = liczba/3
#     return True
#
# with open('liczby.txt','r') as plik:
#     wiersze = plik.read().splitlines()
#     count = 1
#     odpowiedz = ''
#     for liczba in wiersze:
#         if czyJestPotega(liczba):
#             count += 1
#             odpowiedz +=f'{liczba}\n'
#     with open('wyniki4.txt','w') as plik2:
#         plik2.write('Zad 4.1 \n\n\n\n')
#         plik2.write(f'{odpowiedz}')
#         plik2.write(f'Razem - {count}')

# import math

# with open('przyklad.txt','r') as file:
#     for line in file:
#         line = line.strip()
#         suma = 0
#         for num in line:
#             num = int(num)
#             suma += math.factorial(num)
#         if int(line) == suma:
#             print(line)
#
import math
# import copy
# with open('przyklad.txt','r') as plik:
#     wiersze = plik.read().splitlines()
#     pomCiag = list()
#     pomDzielnik = 0
#     ciag = list()
#     maxDzielnik = 1
#     for i in range(len(wiersze)-1):
#         pomDzielnik = math.gcd(int(wiersze[i]),int(wiersze[i+1]))
#         if pomDzielnik != 0:
#             pomCiag.append(wiersze[i])
#         elif len(pomCiag) > len(ciag):
#             ciag = copy.deepcopy(pomCiag)
#             pomCiag = list()
#     print(ciag)
#

file = open("liczby.txt", "r") #jezeli plik nie bedzie istnial, to program zwroc blad
lines = file.read().splitlines() #pozbywamy sie znakow nowego wiersza
file.close() #zamykamy plik
pom = [] #zmienna przechowujaca liczby spelniajace warunki
dzielnik = int(lines[0]) #zmienna przechowujaca aktualny dzielnik (lub pierwsza liczbe ciagu)
pierwszaMax = 0 #zmienna przechowujaca pierwsza liczbe ciagu
dlugoscMax = 0 #zmienna przechowujaca dlugosc ciagu
dzielnikMax = 1 #zmienna przchowujaca dzielnik ciagu

for i in range(1, 500): #iterujemy z pominieciem pierwszej liczby(bo uzylismy ja powyzej)
    num = int(lines[i]) #zamieniamy tekst na liczbe
    nwd = math.gcd(dzielnik, num) #liczymy Najwiekszy Wspolny Dzielnik dla przechowanej liczby/dzielnika
    if nwd != 1: #jeżeli mają wspólny dzielnik (inny niż 1)
        if len(pom) == 0: #sprawdzamy najpierw czy pomocniczy zbior liczb jest pusty (co oznaczałoby, ze w n jest przechowana liczba, a nie dzielnik)
            pom.append(dzielnik) #jezeli tak to od razu dodajemy ta liczbe do zbioru (aby jej nie pominac)
        pom.append(num) #nastepnie dodajemy liczbe z aktualnego wiersza
        dzielnik = nwd #i przypisujemy za n nowy dzielnik
    else:
        if len(pom) > dlugoscMax:#w przeciwnym wypadku sprawdzamy czy pomocniczy zbior jest dluzszy, niz przechowana dlugosc
            dlugoscMax = len(pom) #jezeli tak to zapisujemy jego dlugosc
            dzielnikMax = dzielnik #dzielnik
            pierwszaMax = pom[0] #oraz pierwszy wyraz
        if len(pom) != 0: #jezeli zas pomocniczy zbior nie jest pusty (co oznacza, że wlasnie znalezlismy koniec ciagu)
            if math.gcd(pom[len(pom)-1], num) > 1: #musimy sprawdzic ostatni wyraz i pierwszy nastepnego ciagu
                a = pom[len(pom)-1] #jezeli liczby maja wspolny dzielnik
                pom.clear() #czyscimy zbior pomocniczy
                pom.append(a) #a nastepnie dodajemy do niego od razu dwie liczby
                pom.append(num) #ktore spelniaja warunki zadania
            else:
                pom.clear() #w innym razie po prostu czyscimy zbior pomocniczy
        dzielnik = num #na koniec za dzielnik przypisujemy aktualna liczbe (aby na poczatku petli mozna bylo policzyc nowy NWD)
print("Pierwsza liczba z ciagu: " + str(pierwszaMax) + ", dzielnik " + str(dzielnikMax) + ", dlugosc ciagu: " + str(dlugoscMax))