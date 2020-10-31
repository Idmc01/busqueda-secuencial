def busquedaSecuencial():
    try:
        if isinstance(lista,list) and isinstance(elemento,int):
            posicion = 1
            for i in lista:
                if i == elemento:
                    print("El valor está en la posición: ", posicion)
                    return True
                else:
                    posicion+=1
            return False
        else:
            print("Ingrese un valor válido")
            busquedaSecuencial()
    except:
        print("Ingrese un valor válido")
        busquedaSecuencial()
        
lista = eval(input("Ingrese la lista a evaluar: "))
elemento = int(input("Ingrese el elemento a buscar: "))
print(busquedaSecuencial())

