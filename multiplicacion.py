import math 
lista = []

numero1 = int(input("Ingrese un numero: "))

for i in range(1, numero1 + 1):

    lista.append(i)

result = math.prod(lista)
print("La factorizacion de",numero1,"es",result)