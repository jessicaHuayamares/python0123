
texto="Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen"

#-split
def split():
    lista=texto.split(sep=" ")
    print("SPLIT: ",lista)

#-join
def join():
    lista=texto.split(sep=" ")
    print("JOIN: "," ".join(lista))

#-count
def count():
    print("COUNT: ")
    print("Lorem ",texto.count("Lorem"))
    print("imprentas ",texto.count("imprentas"))

#-find
def find():
    print("FIND: ")
    print("Lorem ",texto.find("Lorem"))
    print("perro ",texto.find("perro"))

#-uppercase
def uppercase():
    print("UPPERCASE: ",texto.upper())

#-lowercase
def lowercase():
    print("LOWERCASE: ",texto.lower())

def solucion2():
    split()
    join()
    count()
    find()
    uppercase()
    lowercase()

#solucion2()

