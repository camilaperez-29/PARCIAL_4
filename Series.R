'''
Este codigo devuelve en pantalla la suma de los 
primeros n  terminos de una serie,en un numero real x.

Párametros de entrada: 
  x = numero real 
  n = numero de terminos a sumar

Autor: Maria Camia Pérez Hincapie
Ultima actualizacion: 22 septiembre, 2021

'''

#definimos la funcion serie(x,n)

serie <- function(x,n){
  
  #inicializamos la serie
  
  sumatoria   <-  0       
  
  #inicializamos el  ciclo
  
  for (i in 1:n) {
    
    termino   <- ((x)^i) / ((i) ^ ((i) ^ (1/i)))
    sumatoria <- sumatoria + termino
    
  }
  
  return(sumatoria)
}



#evaluamos la funcion

serie(2,10)

