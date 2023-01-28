
class Catalogo:
    productos=[]
    def __init__(self,productos=[]):
        self.productos=productos
    
    def agregarProducto(self,p):
        self.productos.append(p)

    def mostrarLista(self):
        for i,c in enumerate(self.productos):
            i+=1
            print(i,c)

class Producto:
    def __init__(self,nombre,id,precio):
        self.nombre=nombre
        self.id=id
        self.precio=precio

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, cuyo id es {self.id} y cuesta S/.{self.precio}"

def solucion4():
    p1=Producto('camisa','01','38')
    p2=Producto('pantalon','02','40')

    print("Catalogo inicial (vacio)")
    cat=Catalogo([])
    cat.mostrarLista()

    print("Catalogo Con el producto 01")
    cat.agregarProducto(p1)
    cat.mostrarLista()

    print("Catalogo agregando el producto 02")
    cat.agregarProducto(p2)
    cat.mostrarLista()

#solucion4()