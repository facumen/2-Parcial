from registro import *


def test():
    opcion = -1
    while opcion != 0:
        if opcion == 1:
            n = int(input('Ingrese la cantidad de trabajos que desea almacenar: '))
            x = [None] * n
            print('¿Desea hacer la carga de datos manual o automatica?')
            opcion_1 = int(input('1.Manual 2.Automatica: '))
            if opcion_1 == 1:
                x = carga_m(x)
            elif opcion_1 == 2:
                x = carga_a(x)
        elif opcion == 2:
            asd = int(input('Ingrese el valor "x" siendo "x" el parametro meor o igual a la nº categorias a mostrar: '))
            punto_2(x, asd)
        elif opcion == 3:
            punto_3(x)
            mostrar(x)
        elif opcion == 4:
            punto_4(x)
        elif opcion == 5:
            id = int(input('Ingrese el numero de identificacion que desea buscar: '))
            cat = int(input('Ingrese la categoria que desea buscar: '))
            if punto_5(x, id, cat):
                print('Se encontro un trabajo con ese id y esa categoria!!')
            else:
                print('No se encontro un trabajo con ese id y esa categoria!!')
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            mostrar(x)
        elif opcion == 9:
            menu()
        opcion = int(input('Ingrese la opcion deseada(9 menu): '))

test()