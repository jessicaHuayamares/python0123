##EJERCICIO 1 
msg = """
"Menu Iterativo"
1) Dibujar un cuadrado 
2) Identificar que números ingresados son múltiplos de 2
3) Identificar a los mayores de edad de los elementos ingresados
4) Salir
"""
while True:
    print(msg)
    op=input("Elija una de las siguientes opciones: ")
    if op =='1':
        cant=int(input("Ingrese el tamaño del cuadrado: "))
        for f in range(cant):
            print (' * '*(cant))

    elif op =='2':
        cant=int(input("Ingresa la cantidad de números a ingresar: "))
        lista=list()
        for v in range(1,cant+1):
            x = int(input(f"Ingrese el item #{v}: "))
            lista.append(x)
    ## print(lista)
        for v in range(cant):
            if(lista[v] % 2==0):
                print(f"El item {v+1} cuyo valor es", lista[v] ,"es multiplo de 2")
    elif op =='3':
        cant=int(input("Ingresa la cantidad de elementos a ingresar: "))
        lista=[]
        for n in range(cant):
            valor = input(f"#{n+1}. Introduce el nombre:")
            edad  = int(input(f"#{n+1}. Introduce su edad:"))
            lista.append([valor,edad])
        print(lista)
        for v in range(cant):
            if (lista[v][1]>=18):
                print(lista[v][0],"es mayor de edad")
    elif op=='4':
        print("¡Hasta luego! Ha sido un placer asistirte")
        break
    else:
        print("Ingrese una opción válida")
