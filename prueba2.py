import os
import time
import collections


def clean():
    """
    Funcion para limpiar pantalla
    """
    os.system('cls')


def sumNode(i):
    """
    Funcion para determinar la Sumatoria por cada nodo
    """
    global groupColor
    value = 0
    view = {i}
    # deque >>> es un contenedor de elemnetos
    # collections >>> El módulo integrado de colecciones que pertenece al standar library de python
    container = collections.deque([(i, {groupColor[i]})])
    while container:
        node, colors = container.popleft()
        value += len(colors)
        for edge in edges[node]:
            if edge not in view:
                view.add(edge)
                container.append((edge, colors | {groupColor[edge]}))
    return value


def assignNodes():
    """
    Funcion para asignar el numero de nodos
    """
    global nodes
    try:
        nodes = int(input('Intruduzca el numero de nodos del arbol: '))
        if nodes > 0 and nodes < 10**5:
            pass
        else:
            print('...........')
            print('ERROR. El numero de nodos debe ser mayor a 0 y, menor o igual a 10^5')
            print('...........')
            time.sleep(3)
            clean()
            assignNodes()
        print('\n Has Creado un arbol de {} nodos'.format(nodes))
        time.sleep(2)
    except ValueError:
        print('...........')
        print('ERROR. Debe introducir un numero entero')
        print('...........')
        time.sleep(3)
        clean()
        assignNodes()


def assignColor():
    """
    Funcion para asignar los colores del primer al ultimo nodo
    """
    global groupColor
    print('NOTA:')
    print('     .- Asigna un color a cada nodo separados por espacios ""')
    print('     .- EJEMPLO: 1 2 3 4 5 6')
    print('Tenemos << {} >> nodos.'.format(nodes))
    groupColor = input('Asigne el grupo de colores: ').split(' ')

    try:
        results = list(map(int, groupColor))
        n = len(results)
        for x in range(0, n):
            if results[x] > 0 and results[x] < 10**5:
                continue
            else:
                print('...........')
                print('ERROR. Debe introducir una operacion mas el numero')
                print('...........')
                time.sleep(3)
                clean()
                assignColor()
        print('\n Correcto!')
        time.sleep(1)
    except ValueError as e:
        print(e)
        print('...........')
        print('ERROR. Debe introducir un numero Entero')
        print('...........')
        time.sleep(3)
        clean()
        assignColor()


def assignEdges():
    """
    Funcion para asignar los enlaces
    """
    global nodes
    global edges

    edges = {i: [] for i in range(nodes)}
    try:
        for i in range(nodes - 1):
            print('NOTA:')
            print('     .-Asigna los enlaces separados por un espacio')
            print('     .-EJEMPLO: Para indicar que el nodo 1 esta conectado con 2')
            print('           Asi: 1 2')
            print('     .-Puedes asignar solo {} enlaces'.format(nodes-1))
            first, second = [
                int(i) - 1 for i in input('Ingresa el {} th  enlace: '.format(i+1)).split(' ')]
            edges[first].append(second)
            edges[second].append(first)
            clean()
        print('\n Correcto!')
        time.sleep(1)
    except ValueError:
        print('...........')
        print('ERROR. Debe introducir un numero Entero')
        print('...........')
        time.sleep(3)
        clean()
        assignEdges()


if __name__ == '__main__':
    """
    EJECUCION PRINCIPAL DEL PROGRAMA
    """
    nodes = 0
    groupColor = []
    edges = {}
    clean()
    assignNodes()
    clean()
    assignColor()
    clean()
    assignEdges()
    clean()
    for i in range(nodes):
        print('\nSumatoria del {} th nodo: {}'.format(nodes+1, sumNode(i)))
