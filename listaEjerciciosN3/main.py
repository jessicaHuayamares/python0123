import problemas.ejercicio_2 as p2
import problemas.ejercicio_3 as p3
import problemas.ejercicio_4 as p4
import problemas.ejercicio_5 as p5
import problemas.ejercicio_6 as p6
import problemas.ejercicio_7 as p7


#Problema1
def ejercicio1():
    if __name__=='__main__':
        
        print("Archivo Principal")
        print("Se ejecutarán los demás problemas")
        sub_main()
    else:
        print("Dependencia")
        
def sub_main():
    print("Problema 02: ")
    p2.solucion2()
    print("Problema 03: ")
    p3.solucion3()
    print("Problema 04: ")
    p4.solucion4()
    print("Problema 05 y 08: ")
    p5.solucion_pro5_prob8()
    print("Problema 06: ")
    p6.solucion6()
    print("Problema 07: ")
    p7.solucion7()



ejercicio1()