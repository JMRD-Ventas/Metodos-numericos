import math

def f(x):
  return x**math.cos(x)

def g(x):
  return math.exp(math.cos(x))

def integral (f, a, b):
  n=int((b-a)/0.001+1)
  h=b-a/n
  x=a
  
  for i in range(n):
    suma += trapecio (f, x, x+h)
    x += h
  return suma

def trapecio (f, a, b):
  h=b-a
  x=(a+b)/2
  return (h/2)(f(a)+f(b)) - h*3/12 * d2 (f, x)

def d2 (f, x):
  h= 0.001
  return (f(x+h)-2*f(c)+f(x-h))/h**2

a=float (input ("dame el limite inferior: "))
b=float (input ("dame el limite superior: "))
print ("la integral de f(x)=  ", integral (f, a, b))
print ("la integral de g(x)=  ", integral (g, a, b))


1. Definir las funciones que se van a integrar (fx y gdx en este caso).

2. Obtener del usuario los límites de integración (límite inferior a y límite superior b).

3. Definir una función "trapecio" que implemente la regla del trapecio compuesta:
    a. Calcular el número de subintervalos (n) en los que se dividirá el intervalo de integración.
    b. Inicializar una variable "suma" en cero.
    c. Iterar sobre los subintervalos:
        i. Calcular el área del trapecio en ese subintervalo usando una función auxiliar.
        ii. Acumular el área en la variable "suma".
    d. Multiplicar la suma acumulada por el ancho de los subintervalos (h) para obtener la aproximación de la integral.

4. Definir una función auxiliar "trapecio_aux" que calcule el área de un solo trapecio:
    a. Calcular el ancho del subintervalo (h).
    b. Calcular el punto medio del subintervalo (x_media).
    c. Aplicar la fórmula del trapecio con corrección del término del error.
    d. Aproximar la segunda derivada en x_media usando una función de diferencias finitas.

5. Definir una función "segunda_derivada" que aproxime la segunda derivada de una función en un punto usando diferencias finitas.

6. Llamar a la función "trapecio" con las funciones fx y gdx, y los límites a y b.

7. Imprimir los resultados de las integrales calculadas.



