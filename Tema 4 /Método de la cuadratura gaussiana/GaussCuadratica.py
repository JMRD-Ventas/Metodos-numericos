
import numpy as np
import matlotlib.pyplot as plt

def f(x):
    return 1-x**2

a=0
b=1

x=np.array([1/3]**0.5,-(1/3)**0.5)
w=np.array([1,1])

u=(b-a)*x/2+(a+b)/2

i=(b-a)*np.sum(w*f(u))/2





print (i)


1. Se define la función f(x) que se desea integrar, en este caso f(x) = 1 - x**2.

2. Se definen los valores de x para la cuadratura gaussiana de orden 2 (grado 2): x = [sqrt(1/3), -sqrt(1/3)].

3. Se definen los pesos w para la cuadratura gaussiana de orden 2: w = [1, 1].

4. Se define el cambio de variable t = (b - a)/2 * v + (a + b)/2, donde a y b son los límites de integración.

5. Se calcula la integral aproximada utilizando la fórmula de la cuadratura gaussiana:
   integral = (b - a)/2 * sum(w[i] * f(t[i]) for i in range(len(x)))

6. Se evalúa la función f(x) en los puntos t[i] obtenidos del cambio de variable.

7. Se multiplica cada evaluación f(t[i]) por su respectivo peso w[i].

8. Se suman todos los términos ponderados w[i]*f(t[i]).

9. Se multiplica la suma por (b - a)/2, que es el factor que queda fuera de la integral después del cambio de variable.

10. Se imprime el resultado de la integral aproximada, que en este caso es 0.6666666666666666, lo cual es la integral exacta de 1 - x**2 en el intervalo [-1, 1].

11. Se menciona que con solo dos evaluaciones de la función (ya que se usa una cuadratura de orden 2), se puede integrar de forma exacta un polinomio de grado hasta 3.

12. Se sugiere que para obtener una aproximación más precisa, se pueden utilizar más valores de x y w, correspondientes a una cuadratura de orden superior.

13. Se muestra cómo se puede utilizar la función integrate del módulo scipy para calcular la integral numérica, la cual probablemente utiliza una cuadratura gaussiana de orden más alto internamente.
