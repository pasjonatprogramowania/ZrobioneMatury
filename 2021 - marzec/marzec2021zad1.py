
kraje = {}
with open("galerie.txt",'r') as plik:
    wszystkieLinie = plik.readlines()
    for w in wszystkieLinie:
        arr = w.rsplit()
        kraj = arr[0]
        kraje[kraj] = 0
    for w in wszystkieLinie:
        arr = w.rsplit()
        kodKraju = arr[0]
        kraje[kodKraju] += 1
print(kraje)