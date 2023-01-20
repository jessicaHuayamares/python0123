#Definiendo diccionarios

biblioteca={
    "nombreBiblioteca":"Roquitas escritas",
    "catLibro":["cientifico","literatura","linguistico","religión","artes","matemáticas"],
    "nombreLibro":{
        "Libro1":{"autor":"autor1",
                "catLibro":["cientifico"],
                "codLibro":"5431",
                "estado":"Libre"
                },
        "Libro2":{"autor":"autor2",
                "catLibro":["literatura"],
                "codLibro":"5432",
                "estado":"Libre"
                },
        "Libro3":{"autor":"autor3",
                "catLibro":["linguistico"],
                "codLibro":"5433",
                "estado":"Prestado"
                },
        "Libro4":{"autor":"autor4",
                "catLibro":["religion"],
                "codLibro":"5434",
                "estado":"Prestado"
                },
        "Libro5":{"autor":"autor5",
                "catLibro":["artes"],
                "codLibro":"5435",
                "estado":"Prestado"
                },
        "Libro6":{"autor":"autor6",
                "catLibro":["matemáticas"],
                "codLibro":"5436",
                "estado":"Prestado"
                }
    },
    "Usuario":{
        "Lucas":{
            "nombreLibro":["Libro3"]
            },
        "Maria":{
            "nombreLibro":["Libro4"]
            },
        "Carlos":{
            "nombreLibro":["Libro5"]
            },
        "Roxssana":{
            "nombreLibro":["Libro6"]
        }
    }
}

msg = """
a) Lista de categorias de libro
b) Nombre de los libros y autores 
c) Cambiar estado de libro a prestado
d) Lista de usuarios de la biblioteca 
"""
print(msg)

op=input("Elija una de las siguientes opciones: ")
if(op =='a' or op =='b'or op=='c' or op=='d'):
    if op =='a':
        print(biblioteca['catLibro'])
    elif op=='b':
        nombreLibros=list(biblioteca["nombreLibro"].items())
        print(nombreLibros)
        for x in biblioteca['nombreLibro'].keys():
            print("-Apartado-")
            print("nombre: ", x)
            autorLibro=biblioteca['nombreLibro'][x]["autor"]
            print("autor:  ", autorLibro)
            
    elif op=='c':
        nomLibro=input("Ingrese el nombre del libro: ")
        listaLibros=list(biblioteca['nombreLibro'].keys())
        ##print(listaLibros)
        if nomLibro in listaLibros:
            ##print("Libro existe")
            estadoLibro=biblioteca['nombreLibro'][nomLibro]['estado']
            if(estadoLibro=='Libre'):
                print("El libro está disponible")
                nombre=input("Ingrese el nombre del usuario al que se le va a prestar el libro: ")
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
    elif op=='d':
        usuarios=biblioteca["Usuario"].keys()
        print(usuarios)
else:
    print("Ingrese una opción válida")




