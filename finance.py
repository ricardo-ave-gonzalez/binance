#!/usr/bin/env python3
# Constantes
ingresos = 12
gastos_administrativos = 5
otros_ingresos = 3
otros_gastos = 1
otros_costos_de_ventas = 0.2

# Datos iniciales del proveedor
materia_prima_base = 2
costos_de_ventas_base = materia_prima_base + otros_costos_de_ventas

# Inicialización del aumento de materia prima
aumento = 0

while aumento >= 0:     
    materia_prima = materia_prima_base + aumento
    costos_de_ventas = materia_prima + otros_costos_de_ventas 
    utilidad_bruta = ingresos - costos_de_ventas
    utilidad_operativa = utilidad_bruta - gastos_administrativos
    utilidad_neta = utilidad_operativa + otros_ingresos - otros_gastos
    print('Aumento:', aumento)    
    print('Materia prima:', materia_prima)
    print('Utilidad bruta:', utilidad_bruta)
    print('Utilidad operativa:', utilidad_operativa)
    print('Utilidad neta:', utilidad_neta)
    print()
    aumento = float(input('Ingrese el aumento de materia prima (ingrese un número negativo para salir): '))
