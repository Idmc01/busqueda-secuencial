def validarListaInt(lista):
    while len(lista) != 0:
        if isinstance(lista[0], int):
            lista = lista[1:]
            continue
        return False
    return True

def busquedaSecuencial():
    try:
        lista = eval(input("Ingrese la lista a evaluar: "))
        if lista != []:
            if isinstance(lista, list) and validarListaInt(lista):
                elemento = int(input("\nIngrese el elemento a buscar: "))
                posicion = 1
                for i in lista:
                    if i == elemento:
                        return print("\nEl valor está en la posición: ", posicion)
                    else:
                        posicion+=1
                else:
                    return print("\nEl valor no se encontró en el vector")
            else:
                print("\nIngrese una lista que contenga únicamente números enteros.\n")
        else:
            print("\nLa lista no puede ser vacía.\n")
        busquedaSecuencial()
    except:
        print("\nIngresó un valor inválido\n")
    busquedaSecuencial()


busquedaSecuencial()
