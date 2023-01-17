##EJERCICIO 1 
print("Menu Iterativo")
msg = """
a) Dibujar un cuadrado 
b) Iteración
c) Mayores de edad
"""
print(msg)
op=input("Elija una de las siguientes opciones: ")
if(op =='a' or op =='b'or op=='c'):
    if op =='a':
        cant=int(input("Ingrese el tamaño del cuadrado: "))
        for f in range(cant):
            print (' * '*(cant))

    elif op =='b':
        cant=int(input("Ingresa la cantidad de numero a ingresar: "))
        lista=list()
        for v in range(1,cant+1):
            x = int(input(f"Ingrese el item {v}:"))
            lista.append(x)
       ## print(lista)
        for v in range(cant):
            if(lista[v] % 2==0):
                print(f"El item {v+1} es Multipo de 2")
            else:
                print(f"El item {v+1} NO es Multipo de 2")
    elif op =='c':
        lista=[["Juan",18],["Maria",12],["Hernan",58],["Lhuana",10]]
        print(lista)
        for v in range(len(lista)):
            if (lista[v][1]>=18):
                print(lista[v][0],"Es mayor de edad")
else:
    print("Ingrese una opción válida")
