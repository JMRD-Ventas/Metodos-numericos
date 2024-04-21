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
  return (h/2)*(f(a)+f(b)) - h**3/12 * d2 (f, x)

def d2 (f, x):
  h= 0.001
  return (f(x+h)-2*f(c)+f(x-h))/h**2

a=float (input ("dame el limite inferior: "))
b=float (input ("dame el limite superior: "))
print ("la integral de f(x)=  ", integral (f, a, b))
print ("la integral de g(x)=  ", integral (g, a, b))


1. Importar la librería numpy como np.
2. Definir una función f(x) que represente la expresión a integrar (en el ejemplo, f(x) = x**2).
3. Solicitar al usuario los siguientes valores:
a: Límite inferior
b: Límite superior
n: Número de trapecios
4. Calcular el espaciamiento h = (b - a) / n
5. Crear un vector de ceros 'x' de tamaño n + 1: x = np.zeros(n+1)
6. Asignar los valores de los extremos: x[0] = a x[n] = b
7. Inicializar la variable suma = 0
8. Realizar un ciclo for desde i = 1 hasta i = n-1: un. Calcular x[i] = x[i-1] + h b. Evaluar f(x[i]) c. Acumular el valor en suma: suma += f(x[i])
9. Calcular el resultado de la integral aplicando la fórmula del trapecio múltiple: integral = (h/2) * (f(x[0]) + 2*suma + f(x[n]))
Imprimir el resultado: print("El resultado de la integral es:", integral)

