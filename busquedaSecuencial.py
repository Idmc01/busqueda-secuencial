#elaborado por: Daniel Araya, Miguel Agüero, Ian Murillo
#Fecha de elaboración: 31/10/2020
#Fecha de última modificación: 31/10/2020
#Versión 3.8.1
#programa principal:
def busquedaSecuencial():
"""
Entradas:
1. La lista a evaluar
2. El número entero a buscar
"""
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

