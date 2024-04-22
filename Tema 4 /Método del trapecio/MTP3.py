import math
def funcion(x):
    return math.sin(x)
def metodo_trapecios(a, b, n):
    h = (b - a) / n
    suma = (funcion(a) + funcion(b)) / 2
    for i in range(1, n):
        suma += funcion(a + i * h)
    return h * suma
limite_inferior = 0
limite_superior = math.pi / 2
numero_divisiones = 1000
resultado_integral = metodo_trapecios(limite_inferior, limite_superior, numero_divisiones)
print("El resultado de la integral es:", resultado_integral)
