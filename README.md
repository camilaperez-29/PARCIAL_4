# PARCIAL_4
CREACIÓN DE FUNCIONES A PARTIR DE SERIES



En este repositorio encontraras el desarrollo de  2 ejercicios basados en la teoría de  series y funciones matemáticas, con el fin de poner en práctica los conocimientos básicos de programacion aprendidos durante el curso de computación 2021 de la Udea.

------
## Pre-requisitos 📝

>Es necesario que para la realizacion de estos ejercicios tengas pre-instalados en tu ordenador [Rstudio](https://www.r-project.org/ "Rstudio") y [PYTHON](https://www.python.org/ "PYTHON"), ya que, los ejercicios se resolvieron en estas 2 interfaces.


## COMENCEMOS 🚀
-----
### **PROBLEMA1**

(FUNCIÓN ZETA DE RIEMMAN $\zeta$ ) En 1735,el matemático suizo Leonhard Euler resolvió un famoso problema en teoría de números, al mostrar que la suma
$$\sum_{k=1}^n\frac{1}{k^2}=1+\frac{1}{2^2}+\frac{1}{3^2}+...+\frac{1}{n^2}\tag{23}$$

se aproxima a $\frac{\pi^2}{6}$,cuando el número de sumandos n se hace "grande". Implemente una funcion llamada `zeta(n)` que evalue la suma. A medida que n se hace "grande", ¿`zeta(n)` se aproxima a $\frac{\pi^2}{6}$?

### *solucion*:

- Primero: definamos la función `zeta(n)` en el lenguaje de Python.


    ``` python
    def zeta(n):

    #inicio de serie
    
    sumatoria  = 0

    #inicio de ciclo

    for k in range (1,(n+1)):

        termino   = 1 / ((k)**2)
        sumatoria = sumatoria + termino
      

    return sumatoria

    ```

- Segundo: evaluemos la función para diferentes n "grandes", *ejemplo:*
    ```python
    funcion = zeta(10000)
    print(funcion)
    ```
    ```python
    1.6448340718480652
    ```
- Tercero: Comparemos el resultado de la función `zeta(n)` con el valor de $\frac{\pi^2}{6}$, para ver que tan aproximado esta del valor real.

    ```python
    valor_real = 1.64493
    print("la diferencia de la funcion zeta respecto al valor original es %f"%(abs(funcion-valor_real)))
    ```
    ```python
    la diferencia de la funcion zeta respecto al valor original es 0.000096
    ```
    
### **RESPUESTA:**
Por lo anterior podemos notar que A medida que n se hace "grande", la diferencia respecto al valor real se hace mas 
pequeña, con lo cual se puede concluir que a medida que n "crece" la funcion `zeta(n)` se aproxima a $\frac{\pi^2}{6}$.







      





