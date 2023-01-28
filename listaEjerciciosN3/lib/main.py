
def fun_recursiva(x:int):
    if(x==1):
        return 1
    else:
        return x+fun_recursiva(x-1)

def dividir(a:int, b:int):
    x=a/b
    return x

def ejercicio6():
    print("Imprimiendo el nombre del archivo en ejecución")
    print("Directorio",__file__,"-> Nombre: ",__name__)

def ejercicio1():
    if __name__=='__main__':
        print("Archivo Principal")
        print("Se ejecutarán los demás problemas")
         
    else:
        print("Dependencia")


#def main():

