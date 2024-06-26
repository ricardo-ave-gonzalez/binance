#!/usr/bin/env python3
import requests
import sqlite3
import datetime
import os

def obtener_ruta_base_datos():
    ruta = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(ruta, 'dbs', 'binance.db')

def obtener_metrica_btc():
    url = 'https://api.binance.com/api/v3/ticker/24hr'
    parametros = {'symbol':'BTCUSDT'} # BITCOIN CODE

    respuesta = requests.get(url, parametros)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        
        lastPrice = float(datos['lastPrice'])
        #metricas = {
        #    'precio actual': float(datos['lastPrice'])
        #}
        #return metricas
        
        return lastPrice

    else:
        print(f"Error al obtener las metricas y/o datos: {respuesta.status_code}")

def crear_basecita(ruta_base_datos):
    try:
        conexion = sqlite3.connect(ruta_base_datos)
        cursor = conexion.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin(
                            collectTS INTEGER DEFAULT (strftime('%s', 'now')),
                            price REAL,
                            fecha DATE
                       )''')
        conexion.commit()
        cursor.close()
        conexion.close()
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")

def guardar_datos(lastPrice, fecha_actual, ruta_base_datos):
    try:
        conexion = sqlite3.connect(ruta_base_datos)
        cursor = conexion.cursor()

        cursor.execute("INSERT INTO bitcoin (price, fecha) VALUES (?,?)", (lastPrice, fecha_actual))
        conexion.commit()
        cursor.close()
        conexion.close()

        print("Se persistieron correctamente los datos de binance")
    except sqlite3.Error as e:
        print(f"Error al persistir los datos en dbs/bacesita: {e}")

lastPrice = obtener_metrica_btc()

if lastPrice is not None:
    ruta_base_datos = obtener_ruta_base_datos()
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    crear_basecita(ruta_base_datos)
    guardar_datos(lastPrice, fecha_actual, ruta_base_datos)
