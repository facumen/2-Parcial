import random
titles = 'Ing. Sistemas', 'Teacher', 'Mecanico'
author = 'Juan', 'Silvio', 'Frodo', 'Bush', 'El profe de AED', 'Es el mejor', 'Franco', 'Gabriela'


class Trabajo:
    def __init__(self, numero, titulo, autor, categoria):
        self.numero = numero
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria


def carga_m(vec):
    for i in range(len(vec)):
        numero = int(input('Ingrese el numero de identificacion: '))
        titulo = input('Ingrese el titulo del trabajo: ')
        autor = input('Ingrese el autor principal del trabajo: ')
        categoria = valid('Ingrese la categoria del tranajko (1, 15): ', 1, 15)
        vec[i] = Trabajo(numero, titulo, autor, categoria)
        print('-' * 100)
    return vec


def carga_a(vec):
    for i in range(len(vec)):
        numero = random.randint(1, 100)
        titulo = random.choice(titles)
        autor = random.choice(author)
        categoria = random.randint(1, 15)
        vec[i] = Trabajo(numero, titulo, autor, categoria)
    return vec


def mostrar(vec):
    for i in range(len(vec)):
        print('-' * 100)
        print('El numero de identificacion es: ', vec[i].numero)
        print('El titulo del trabajo es: ', vec[i].titulo)
        print('El autor principal del trabajo es: ', vec[i].autor)
        print('La categoria del trabajo es: ', vec[i].categoria)
        print('-' * 100)

def menu():
    print('1- Cargar el arreglo pedido con los datos de los n trabajos.')
    print('2- Mostrar los datos de todos los trabajos cuyo número de categoría sea menor o igual a x, '
          'siendo x un valor cargado por teclado y pasado por parámetro.')
    print('3- Mostrar todos los datos, ordenados de menor a mayor según el nombre del autor.')
    print('4- Determinar y mostrar la cantidad de trabajos por categoría (un contador para sumar los trabajos tipo 1,'
          ' otro para el tipo 2, otro para el tipo 3, etc.).')
    print('5- Determinar si existe un trabajo con número de identificación igual a id, pero cuya categoría sea'
          ' igual a cat.')
    print('8- Mostrar vector x')
    print('9- Menu')
    print('0- Salir')


def valid(msje, inf, sup):
    n = -1
    while n < inf or n > sup:
        n = int(input(msje))
        if n < inf or n > sup:
            print('Escriba un valor valido por favor')
    return n


def punto_2(vec, x):
    nvo_vec = []
    flag = False
    for i in range(len(vec)):
        if x >= vec[i].categoria:
            nvo_vec.append(vec[i])
            flag = True
    if not flag:
        print('No se encontro trabajo con x menor a la categoria')
    mostrar(nvo_vec)


def punto_3(vec):
    for i in range(len(vec) - 1):
        for j in range(i + 1, len(vec)):
            if vec[i].autor > vec[j].autor:
                vec[i], vec[j] = vec[j], vec[i]


def punto_4(vec):
    conteo = [0] * 15
    for i in range(len(vec)):
        pos = vec[i].categoria
        conteo[pos - 1] += 1
    for i in range(len(conteo)):
        if conteo[i]:
            print('Existen ', conteo[i], 'trabajos para la categoria', i + 1)


def punto_5(vec, id, cat):
    for i in range(len(vec)):
        if vec[i].numero == id and vec[i].categoria == cat:
            return True
    else:
        return False

