# Método del trapecio

# Concepto:
# Este método se basa en la aproximación del área bajo la curva mediante trapecios. 
# Divide el área bajo la curva en varios trapecios y luego -
# calcula la suma de las áreas de estos trapecios para aproximar la integral definida.

#Fórmula: 
    # [(DeltaX]* f(a)+f(b) para solo una interaccion
    # [(DeltaX)* [f(x0)+2f(x1)+2f(x2)+...+ 2f(xn-1)+f(xn)+] para varias interacciones

# Significado de la simbología:

#    - f(x0): Funcion evaluada con intervalo a.
#    - f(x1,x2): Funciom evaludada con n.
#    - ( DeltaX o h): Funcion evaluada (b-a)/n
#    - ( a ) y ( b ): Extremos del intervalo de integración.
#    - ( n ): Número de subintervalos en los que se divide el intervalo.


import numpy as np

# Paso 1: Define tu función en forma de texto.
String = "(-x^2 + 8x - 12)"

# Paso 2: Definir la función
def f(x):
    return -x**2+8*x-12

a, b = 3, 5
n = 2

# Paso 3: Definir DeltaX
def DeltaX(a, b, n):
    h = (b - a) / n
    suma = (f(a) + f(b)) / 2
# Paso 4: Funcion evaluada en un ranga desde 1 a n

    for i in range(1, n):
        suma += f(a + i * h)
    return h * suma

# Aplicación de los métodos
resultado_trapecio = DeltaX(a, b, n)


# Resultados
print("")
print("La ecuación ingresada es: ", String)
print("El parámetro a o límite inferior es: ", a)
print("El parámetro b o límite superior es: ", b)
print("El n de interacciones es: ", n)
print("El resultado aplicando el método del trapecio es:", resultado_trapecio)
print("Bibliográfia: https://www.youtube.com/watch?v=6A6dtNJbdT0&ab_channel=Matem%C3%A1ticasPi%C3%B1a%2aProfePi%C3%B1a%2a")
print("")