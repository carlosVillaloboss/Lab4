from NodListSimple import ListaSimple
from NodListDoble import ListaDoble

def main():
    # Crear lista para almacenar los números pares del 1 al 20
    lista_numeros = ListaDoble()

    # Agregar números pares del 2 al 20
    for num in range(2, 21, 2):
        lista_numeros.addLast(num)

    print("Lista inicial con números pares del 2 al 20:")
    lista_numeros.printList()

    # Eliminar los números 10 y 20
      
    lista_numeros.remove(10)
    lista_numeros.remove(20)

    print("\nLista después de eliminar 1, 10 y 20:")
    lista_numeros.printList()


main()