#EJERCICIO3: Definir una función que retorne el mayor valor al ingresar 2 numeros 
numeros = []
# Ingresamos 2 numeros
for n in range(2):
    valor = float(input(f"Introduce el número #{n+1}: "))
    numeros.append(valor)
# defino mi función
def mayor():
    mayor = numeros[0]
    if mayor<numeros[1]:
        mayor =numeros[1]
    return f"Mayor valor {mayor}"
# llamo mi función
print(mayor())