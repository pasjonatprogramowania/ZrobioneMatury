import math
# with open('dane.txt','r') as plik:
#     wiersze = plik.read().splitlines()
#     komurki = []
#     for w in wiersze:
#         komurki += w.split()
#     war = list(map(int,komurki))
#     print(min(war))
#     print(max(war))
#     with open('wyniki6.txt','w') as plik2:
#         plik2.write(f"zad 6.1 \n\n\n\n min - {min(war)} \n max - {max(war)} \n")
#
# with open('dane.txt','r') as plik:
#     wiersze = plik.read().splitlines()
#     wierszeDoUsunacia = 0
#     for w in wiersze:
#         dane = w.split()
#         odd = dane[::-1]
#         for i in range(len(dane)):
#             if odd[i] != dane[i]:
#                 wierszeDoUsunacia += 1
#                 break
#     with open('wyniki6.txt','a') as plik2:
#         plik2.write(f"zad 6.2 \n\n\n\n {wierszeDoUsunacia} \n")
#

# with open('przyklad.txt','r') as plik:
#     wiersze = plik.read().splitlines()
#     dane = []
#     kontrastujace = 0
#     for w in wiersze:
#         dane.append(w.rsplit())
#     for y in range(len(dane) - 1):
#         for x in range(len(dane[y]) - 1):
#             a = int(dane[y][x])
#             b = int(dane[y][x + 1])
#             c = int(dane[y + 1][x])
#         if abs(a - b) > 128 or abs(a - c) > 128:
#             kontrastujace += 1
#     print(kontrastujace)

# def nearContrasting(x, y, all):
#     if x != 0:
#         if abs(all[x][y] - all[x - 1][y]) > 128:
#             return True
#     if x != 199:
#         if abs(all[x][y] - all[x + 1][y]) > 128:
#             return True
#     if y != 319:
#         if abs(all[x][y] - all[x][y + 1]) > 128:
#             return True
#     if y != 0:
#         if abs(all[x][y] - all[x][y - 1]) > 128:
#             return True
#     return False
#
# file = open("przyklad.txt", "r").read().split('\n')
# all = []
# counter = 0
# contrasting = 0
# for line in file:
#   all.append(list(map(int,line.rsplit())))
# for i in range(200):
#     for j in range(320):
#         if nearContrasting(i, j, all):
#             contrasting += 1
# print("Punktów kontrastujących: " + str(contrasting))

# with open('przyklad.txt','r') as plik:
#     wiersze = plik.read().splitlines()
#     dane = []
#     pomciag = 1
#     ciag = 1
#     for w in wiersze:
#         dane = w.split()
#         for i in range(len(dane)-1):
#             a = dane[i]
#             b = dane[i+1]
#             if a == b:
#                 pomciag += 1
#             elif pomciag > ciag:
#                 ciag = pomciag
#                 pomciag = 1
#             else:
#                 pomciag = 1
#         if pomciag > ciag:
#             ciag = pomciag
#             pomciag = 1
#         pomciag = 1
#     print(ciag)
#

