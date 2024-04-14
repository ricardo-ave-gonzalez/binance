#!/usr/bin/env python3
# Solicitamos al usuario que ingrese la masa y la fuerza neta
# masa = float(input("Ingrese la masa del objeto (en kilogramos): "))
# fuerza_neta = float(input("Ingrese la fuerza neta aplicada al objeto (en Newtons): "))

# Calculamos la aceleración usando la segunda ley de Newton
# aceleracion = fuerza_neta / masa

# Imprimimos el resultado
# print("La aceleración del objeto es:", aceleracion, "m/s^2")


def calcular_masa(fuerza_neta, aceleracion):
    """
    Calcula la masa de un objeto dado su fuerza neta y su aceleración.
    """
    masa =  fuerza_neta / aceleracion
    return masa

def calcular_aceleracion(fuerza_neta, masa):
    """
    Calcula la aceleración de un objeto dado su fuerza neta y su masa.
    """
    aceleracion = fuerza_neta / masa
    return aceleracion

def main():
    print("--------------------------------------------------------------------------------")
    print("Este programa calcula la aceleración de un objeto dado su fuerza neta y su masa.")
    fuerza_neta = float(input("Ingrese la fuerza neta aplicada sobre el objeto (en Newtons): "))
    masa = float(input("Ingrese la masa del objeto (en kilogramos): "))

    aceleracion = calcular_aceleracion(fuerza_neta, masa)
    print("La aceleración del objeto es:", round(aceleracion), "m/s^2")

    print("----------------------------------------------------------------------------------")
    print("Este programa calcula la masa de un objeto dado su fuerza neta y su aceleracion.")
    fuerza_neta = float(input("Ingrese la fuerza neta aplicada sobre el objet (en Newtons):"))
    acelaracion = float(input("Ingrese la aceleracion del objeto en metros por segundo al cuadrado:"))

    masa = calcular_masa(fuerza_neta,acelaracion)
    print("La masa del objeto es de :", round(masa), "kilogramos")
if __name__ == "__main__":
    main()
