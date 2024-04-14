#!/usr/bin/env python3
# Solicitamos al usuario que ingrese la masa y la fuerza neta
# masa = float(input("Ingrese la masa del objeto (en kilogramos): "))
# fuerza_neta = float(input("Ingrese la fuerza neta aplicada al objeto (en Newtons): "))

# Calculamos la aceleración usando la segunda ley de Newton
# aceleracion = fuerza_neta / masa

# Imprimimos el resultado
# print("La aceleración del objeto es:", aceleracion, "m/s^2")

def calcular_aceleracion(fuerza_neta, masa):
    """
    Calcula la aceleración de un objeto dado su fuerza neta y su masa.

    Args:
    - fuerza_neta (float): La fuerza neta aplicada sobre el objeto (en Newtons).
    - masa (float): La masa del objeto (en kilogramos).

    Returns:
    - aceleracion (float): La aceleración del objeto (en m/s^2).
    """
    aceleracion = fuerza_neta / masa
    return aceleracion

def main():
    print("Este programa calcula la aceleración de un objeto dado su fuerza neta y su masa.")
    fuerza_neta = float(input("Ingrese la fuerza neta aplicada sobre el objeto (en Newtons): "))
    masa = float(input("Ingrese la masa del objeto (en kilogramos): "))

    aceleracion = calcular_aceleracion(fuerza_neta, masa)
    print("La aceleración del objeto es:", aceleracion, "m/s^2")

if __name__ == "__main__":
    main()
