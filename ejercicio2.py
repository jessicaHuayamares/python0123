#EJERCICIO 2
biblioteca={
    "nombreBiblioteca":"Roquitas escritas",
    "catLibro":["cientifico","literatura","linguistico","religión","artes","matemáticas"],
    "nombreLibro":{
        "EL ORIGEN DE LAS ESPECIES":{"autor":"Charles Darwin",
                "catLibro":["cientifico"],
                "codLibro":"5431",
                "estado":"Libre"
                },
        "DON QUIJOTE DE LA MANCHA":{"autor":"Miguel de Cervantes",
                "catLibro":["literatura"],
                "codLibro":"5432",
                "estado":"Libre"
                },
        "REGLAS DEL LENGUAJE":{"autor":"Juan Cabrera Ruiz",
                "catLibro":["linguistico"],
                "codLibro":"5433",
                "estado":"Prestado"
                },
        "LA MAGIA Y EL MILAGRO":{"autor":"Pedro Montalvo Sanchez",
                "catLibro":["religion"],
                "codLibro":"5434",
                "estado":"Prestado"
                },
        "HISTORIA DEL ARTE":{"autor":"Ernst Gombrich",
                "catLibro":["artes"],
                "codLibro":"5435",
                "estado":"Prestado"
                },
        "LA MAGIA DE LOS NÚMEROS":{"autor":"Jordi Deulofeu Piquet",
                "catLibro":["matemáticas"],
                "codLibro":"5436",
                "estado":"Prestado"
                }
    },
    "Usuario":{
        "LUCAS":{
            "nombreLibro":["REGLAS DEL LENGUAJE"]
            },
        "MARIA":{
            "nombreLibro":["LA MAGIA Y EL MILAGRO"]
            },
        "CARLOS":{
            "nombreLibro":["HISTORIA DEL ARTE"]
            },
        "ROXSSANA":{
            "nombreLibro":["LA MAGIA DE LOS NÚMEROS"]
        }
    }
}

msg = """
Menú
1) Lista de categorias de libro
2) Nombre de los libros y autores 
3) Cambiar estado de libro a prestado
4) Lista de usuarios de la biblioteca
5) Salir
"""
while True:
    print(msg)
    op=input("Elija una de las siguientes opciones: ")
    if op =='1':
        print(biblioteca['catLibro'])
    elif op=='2':
        nombreLibros=list(biblioteca["nombreLibro"].items())
         ##print(nombreLibros)
        for x in biblioteca['nombreLibro'].keys():
            print("-Apartado-")
            print("nombre: ", x)
            autorLibro=biblioteca['nombreLibro'][x]["autor"]
            print("autor:  ", autorLibro)
    elif op=='3':
        nomLibro=input("Ingrese el nombre del libro: ").upper()
        listaLibros=list(biblioteca['nombreLibro'].keys())
        ##print(listaLibros)
        if nomLibro in listaLibros:
            ##print("Libro existe")
            estadoLibro=biblioteca['nombreLibro'][nomLibro]['estado']
            if(estadoLibro=='Libre'):
                print("El libro está disponible")
                nombre=input("Ingrese el nombre del usuario al que se le va a prestar el libro: ").upper()
                usuarios=list(biblioteca["Usuario"].keys())
                if(nombre in usuarios):
                    agregarLibro=biblioteca["Usuario"][nombre]["nombreLibro"]
                    agregarLibro.append(nomLibro)
                    biblioteca['nombreLibro'][nomLibro]['estado']={'estado':'Prestado'}
                    print(biblioteca['nombreLibro'][nomLibro]['estado'])
                    print("Cambio de estado realizado correctamente")
                    print(biblioteca)
                else:
                    print("usuario no existe")
            else:
                print("No se pudo cambiar de estado, porque el libro ya se encuentra prestado")
        else:
            print("Libro no existe") 
    elif op=='4':
        usuarios=biblioteca["Usuario"].keys()
        print(usuarios)
    elif op=='5':
        print("¡Hasta luego! Ha sido un placer asistirte")
        break
    else:
        print("Ingrese una opción válida")




