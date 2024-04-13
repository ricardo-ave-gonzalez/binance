#!/usr/bin/env python3
# Solicitamos al usuario que ingrese la masa y la fuerza neta
masa = float(input("Ingrese la masa del objeto (en kilogramos): "))
fuerza_neta = float(input("Ingrese la fuerza neta aplicada al objeto (en Newtons): "))

# Calculamos la aceleración usando la segunda ley de Newton
aceleracion = fuerza_neta / masa

# Imprimimos el resultado
print("La aceleración del objeto es:", aceleracion, "m/s^2")
