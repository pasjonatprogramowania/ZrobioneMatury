n = 5
A = [1,2,3,4,5,6,8,1,-5,-22,9,-12]
B = [1,4,5,6,8,9,4,2,3]
# def a(x):
#     if x > 1:
#         for i in range(2,x):
#             if x%i==0:
#                 return False
#         return True
#     return False
#
# for b in A:
#     if a(b):
#         print(b)

# def a(x):
#     for i in range(len(x)):
#         for j in range(len(x)-i-1):
#             if x[j] > x[j+1]:
#                 t = x[j]
#                 x[j] = x[j+1]
#                 x[j+1] = t
# a(A)
# def a(x):
#     a = 0
#     b = 1
#     for i in range(0,x):
#         t = a
#         a = b
#         b = t + b
#     return a
# print(a(10))
# def sz(w,k):
#     wynik = ''
#     for i in w:
#         wynik += chr((ord(i)+k-65)%26+65)
#     return wynik
# def dsz(w,k):
#     k *= -1
#     return sz(w,k)
# a = 'ALA'
# k = 4
# print(sz(a,k))
# print(dsz(sz(a,k),k))

# def nwd(a,b):
#     while b!=0:
#         t = a
#         a = b
#         b =t%b
#     return b
# print(nwd(5,10))
# def silnia(x):
#     if x == 1:
#         return x
#     elif x<1:
#         return None
#     return x*silnia(x-1)


# print(silnia(10))
# import math
# print(math.factorial(10))

import statistics

