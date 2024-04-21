from math import *

def evaluacion (x):
    copia=funcion.copy()
    for j in range (len(copia)):
        if copia [j] == "x":
            copia [j]==x
    return eval ("".join(copia))

            
funcion = list (input ("cual es la integral/funcion?  "))
a = float (input ("cual es el intervalo inferior?  "))
b = float (input ("cual es el intervalo superior?  "))
n = float (input ("cual es el valor de n?  "))

h= (b-a)/n
total=0


for i in range (1,n):
    x=a(i*h)
    if (i%2==0):
        total +=2*evaluacion (x)
        
    else:
        total +=4*evaluacion (x)
        
total+=evaluacion (a)+evaluacion (b)
total = total ((11/3)*h)

print ("resultado de la aporximacion = {total}")



1. Se presenta el método de Simpson un tercio, que permite aproximar la integral de una función.

2. Se mencionan los puntos que se deben tomar en cuenta: x0, x1, x2 (donde x1 está en el medio del intervalo [x0, x2]).

3. Se muestra la fórmula del método de Simpson un tercio para calcular la integral aproximada en el intervalo [x0, x2].

4. Se menciona que existe un error de aproximación, dado por una fórmula que involucra la cuarta derivada evaluada en un punto ξ entre x0 y x2.

5. Se da un ejemplo con la función f(x) = 2/(x^2 - 4) y se quiere calcular la integral en el intervalo [0, 0.35].

6. Se determinan los valores de x0 = 0, x1 = 0.175 y x2 = 0.35.

7. Se evalúa la función f(x) en x0, x1 y x2.

8. Se reemplaza en la fórmula del método de Simpson un tercio con los valores obtenidos.

9. Se realiza la operación y se obtiene la aproximación de la integral como -0.1767.

10. Se menciona que se mostrará cómo aplicar el método con un código en Python.

11. Se pide al usuario ingresar la función a integrar y se convierte a una lista.

12. Se piden los límites inferior y superior del intervalo, y el valor de n.

13. Se calcula el valor de h.

14. Se crea una variable "total" inicializada en 0 para almacenar el resultado.

15. Se realiza un ciclo for que evalúa la función en x0, x1, ..., xn.

16. Dentro del ciclo, se determina si i es par o impar para multiplicar por 2 o 4, respectivamente.

17. Se crea una función "evaluacion" que recibe x y evalúa la función ingresada en ese valor de x.

18. Dentro de "evaluacion", se hace una copia de la función, se reemplaza x por el valor dado, se convierte a cadena y se evalúa.

19. El resultado de la evaluación se multiplica por 2 o 4 y se suma a "total".

20. Después del ciclo, se suma la evaluación en los límites inferior y superior a "total".

21. Se multiplica "total" por h/3 y se almacena en "total".

22. Se imprime el valor final de "total", que es la aproximación de la integral.

23. Se muestran dos ejemplos de uso del código.
