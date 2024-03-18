import math 
def factorizacion(numero):
    lista = []

    for i in range(1, numero + 1):
        lista.append(i)
        
    resultado = math.prod(lista)
    return resultado

numero1 = int(input("Ingrese un numero"))
resultado_factorial = factorizacion(numero1)
print ("La factorizacion de", numero1, "es", resultado_factorial)