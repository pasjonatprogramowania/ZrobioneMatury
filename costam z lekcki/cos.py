def horner(poly, n, x):
    result = poly[0]
    for i in range(1, n):
        result = result * x + poly[i]
    return result
poly = [2, -6, 2, -1]
x = 3
n = len(poly)

print("Value of polynomial is ", horner(poly, n, x))
