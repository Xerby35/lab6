from math import pi
def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)
def sine_x(x_deg, n):
    x = x_deg * (pi / 180)
    result = 0
    for i in range(n):
        term = (lambda n: ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1))(i)
        result += term
    return result
harmonic_sum = 0
def harmonic(n):
    global harmonic_sum
    if n == 0:
        return
    harmonic(n - 1)
    harmonic_sum += 1 / n
x=int(input("Faktöriyel için bir sayı giriniz.""\n"))
print("Question1: Girdiğiniz sayının faktöriyeli =", factorial(x))

x=int(input("Sin(x) için değer girin.""\n"))
n=int(input("Sin(x) için terim sayısı girin.""\n"))
print("Question2: sin(",x, ")yaklaşık değeri (",n, ") terim:".format(x, n), sine_x(x,n))
harmonic_sum = 0
x = int(input("Harmonik sayı için deger girin""\n"))
harmonic(x)
print("Question3: harmonik değer:".format(x), harmonic_sum)
