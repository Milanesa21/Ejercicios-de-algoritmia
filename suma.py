def suma(numero1, numero2):
        resultado = numero1 - (-numero2)
        return resultado
    
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

resultado = suma(numero1,numero2)
print("La suma de los numeros es: ", resultado)