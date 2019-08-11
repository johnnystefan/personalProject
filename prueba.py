import os
import time


def clean():
    """
    Funcion para limpiar pantalla.
    """
    os.system('cls')


def addListNumbers(number):
    """
    Funcion para agregar items al list_numbers.
    """
    list_numbers.append(number)
    median()


def removeListNumbers(number):
    """
    Funcion para eliminar items de list_numbers.
    NOTA: Dado el caso de que no se encuentre el item en la lista 
          la salida sera una advertencia.
    """
    try:
        list_numbers.remove(number)
        median()
    except:
        print('Wrong!')


def median():
    """
    Funcion para calcular la media de una lista ordenada.
    
    NOTA: 
        .- Si la longitud de lista es un numero "IMPAR", se define la media 
        como el número del medio después de ordenarlos.
        .- Si la longitud de lista es un numero "PAR", se define la media 
        como el promedio de los dos números del medio después de ordenarlos.
    """
    if numberOperations > 0:
        list_sorted = sorted(list_numbers)
        m = len(list_numbers)
        if m > 0:
            if m % 2 == 0:
                result = format(
                    0.5*(list_sorted[m//2] + list_sorted[(m//2)-1]), '.100g')
                return print("Media: {}".format(result))
            else:
                return print("Media: {}".format(list_sorted[m//2]))
        else:
            print('Wrong!')

def assignOperations(operations, attempts):
    """
    Funcion para recibir la accion u operaccion que se ejecutara sobre la lista de numeros
    
    NOTA:
        .- Estas Acciones pueden ser:
            1.- AGREGAR (ADD)
            2.- ELIMINAR (REMOVE)
    """
    n = operations
    tried = attempts
    # INTMAX ENTERO positivo que representa el valor MAXIMO 
    # para el valor de x como un entero de 32 bits.
    INTMAX = 4294967295
    for x in range(0, operations):
        print('NOTA:')
        print('\nPuedes: AGREGAR o ELIMINAR.')
        print('     .- Para agregar: Debes digitar el caracter "a" precedido del numero "x" a agregar a la lista')
        print('     .- Para eliminar: Debes digitar el caracter "r" precedido del numero "x" a eliminar de la lista')
        print('Te quedan << {} >> operaciones sobre la lista.'.format(n))
        print('Lista de Numeros: {}'.format(sorted(list_numbers)))
        operation = input('Intruduzca la operacion {} a ejecutar: '.format(1+tried))

        try:
            number = int(operation.strip('ra'))
            if operation[0] == 'a' or operation[0] == 'r' and (number >= 0 and number <= INTMAX):
                if operation[0] == 'a':
                    addListNumbers(number)
                    tried = tried+1
                    n = n-1
                    time.sleep(2)
                elif operation[0] == 'r':
                    tried = tried+1
                    n = n-1
                    removeListNumbers(number)
                    time.sleep(2)
            else:
                print('...........')
                print('ERROR. Debe introducir una operacion mas el numero')
                print('...........')
                time.sleep(3)
                clean()
                assignOperations(n, tried)

        except ValueError as e:
            print(e)
            import pdb
            pdb.set_trace()
            print('...........')
            print('ERROR. Debe introducir un numero entero')
            print('...........')
            time.sleep(3)
            clean()
            assignOperations(n, tried)

        clean()


def assignNumberOperations():
    """
    Funcion para obtener la cantidad de operaciones que se realizar
    """
    global numberOperations
    try:
        operations = int(input('Intruduzca el numero de operaciones: '))
        if operations > 0 and operations < 10**5:
            numberOperations = operations
        else:
            print('...........')
            print('ERROR. El numero de operaciones debe ser mayor a 0 y, menor o igual a 10^5')
            print('...........')
            time.sleep(3)
            clean()
            assignNumberOperations()
    except ValueError:
        print('...........')
        print('ERROR. Debe introducir un numero entero')
        print('...........')
        time.sleep(3)
        clean()
        assignNumberOperations()


if __name__ == '__main__':
    """
    EJECUCION PRINCIPAL DEL PROGRAMA
    """
    list_numbers = []
    clean()
    numberOperations = 0
    assignNumberOperations()
    clean()
    assignOperations(numberOperations, 0)
