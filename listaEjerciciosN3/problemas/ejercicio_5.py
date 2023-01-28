#-Una función recursiva de suma de los n primeros números
#-Una función que me permita dividir 2 números.

# from main2 import fun_recursiva, dividir
import os

#Problema5
def fun_recursiva(x:int):
    if(x==1):
        return 1
    else:
        return x+fun_recursiva(x-1)

def dividir(a:int, b:int):
    x=a/b
    return x

def solucion_pro5_prob8():
    try:
        num=int(input("Se hará una suma de los x primero números, ingresa un numero: "))
        print(fun_recursiva(num))
        print("Se dividiran dos números")
        num1=int(input("Ingresa numero1: "))
        num2=int(input("Ingresa numero2: "))
        print(dividir(num1,num2))
    except:
        print("Ha ocurrido un error")
    else:
        print("Ruta del directorio de trabajo actual: ",os.getcwd())
    finally:
        print("Proceso terminado")
        
# solucion_pro5_prob8()