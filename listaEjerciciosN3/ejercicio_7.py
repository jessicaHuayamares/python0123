class Producto():
    def __init__(self, nombre,codigo:str):
        self.nombre=nombre
        self.codigo=codigo
    
    def __str__(self) -> str:
        codigo=self.codigo.split(sep="-")
        return f"Nombre: {self.nombre}\nCodigo: {self.codigo}\nPais: {codigo[0]}\nLote: {codigo[1]}"

def solucion7():
    p1=Producto('Polos','PERU-0004-2023')
    p2=Producto('Pantalones','URUGUAY-0123-2023')
    print(p1)
    print(p2)

#solucion7()
