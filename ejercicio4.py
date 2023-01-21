##Definir una función que imprima los argumentos ingresados desde la linea de comandos
import sys

op=int(input("Digite la cantidad de argumentos que ingresará: "))
lista=[]
def ingreso(op):
    for x in range(0,op):
        lista.append(input(f"Argumento #{x+1}: "))
    return lista

def imprimirArgumentos(*args):
    for arg in args:
        print(arg)
        
imprimirArgumentos(ingreso(op))
