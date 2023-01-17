#Definir una función que retorne
# el mayor valor
#al ingresar 2 numeros

# defino mi función
def mayor():
    a=int(input("Ingrese un número: "))
    b=int(input("Ingrese un número: "))
    if a>b:
        return a
    elif b>a:
        return b
    else:
        print("Error: Valores iguales")
# llamo mi función
fun=mayor()
print("Mayor valor:")
print(fun)