with open("przyklad.txt",'r') as plik:
    wiersze = plik.readlines()
def sprawdzTypInstrukcji(instrukcje):
    maxCiag = 0
    maxWyraz = ""

    poprzedniaInstrukcja = ""
    aktualnaInstrukcja = ""
    aktualnaDlugoscCiagu = 0
    for instrukcja in enumerate(instrukcje):
        instrukcja = instrukcja[1].rsplit()
        poprzedniaInstrukcja = aktualnaInstrukcja
        aktualnaInstrukcja = instrukcja[0]
        if poprzedniaInstrukcja == aktualnaInstrukcja:
            aktualnaDlugoscCiagu += 1
            poprzedniaInstrukcja = instrukcje
        else:
            if aktualnaDlugoscCiagu > maxCiag:
                maxCiag = aktualnaDlugoscCiagu
                maxWyraz = poprzedniaInstrukcja
    return (maxCiag,maxWyraz)


print(sprawdzTypInstrukcji(wiersze))