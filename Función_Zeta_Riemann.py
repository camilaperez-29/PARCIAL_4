'''
Este codigo devuelve en panatalla 
la funcion Zeta de Riemann para obtener ((pi)**2)/6.

Párametros de entrada: 
    n = número de sumas que se calculan para obtener ((pi)**2 / (6)).
   
Autor: Maria Camila Perez Hincapie
Ultima actualizacion: 22 septiembre, 2021

'''

def zeta(n):

    #inicio de serie
    
    sumatoria  = 0

    #inicio de ciclo

    for k in range (1,(n+1)):

        termino   = 1 / ((k)**2)
        sumatoria = sumatoria + termino
      

    return sumatoria


'''
 A medida que n se hace "grande", ¿ zeta(n) se aproxima a ((pi)**2 / (6)) ?

'''

#Evaluamos la funcion para un "n grande"

x = zeta(1000000)
print(x)

#comparamos el resultado de la funcion respecto al valor real

valor_real = 1.64493
print("la diferencia de la funcion zeta respecto al valor original es %f"%(abs(x-valor_real)))


'''
Respuesta : En definitiva. A medida que n se hace "grande", la diferencia respecto al valor real se hace mas 
            pequeña, con lo cual se puede concluir que a medida que n "crece" la funcion zeta(n) se aproxima 
            a ((pi)**2 / (6))

'''




