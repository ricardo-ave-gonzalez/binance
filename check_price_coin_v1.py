#!/usr/bin/env python3
# Telegram

import requests
import sys

def obtener_precio_binance(moneda: str) -> float:
    """Consulta el precio actual de la moneda en Binance."""
    url = "https://api.binance.com/api/v3/ticker/24hr"
    parametros = {"symbol": f"{moneda}USDT"}
    respuesta = requests.get(url, params=parametros)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        return float(datos["lastPrice"])
    else:
        print(f"Error al obtener el precio: {respuesta.status_code}")
        return None

def enviar_alerta(mensaje: str):
    """Envía un mensaje a Telegram."""
    TOKEN = "token"
    CHAT_ID = "chatId"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    #para obtener el id e info de mi botchat
    #url_get = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    #print(requests.get(url_get).json())

    data = {"chat_id": CHAT_ID, "text": mensaje}

    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Error al enviar mensaje: {e}")

def guardar_log(mensaje: str):
    """Guarda los mensajes en un archivo log con fecha y hora en logs/"""
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)  # Crea el directorio si no existe

    log_file = os.path.join(log_dir, f"binance_{datetime.now().strftime('%Y%m%d')}.log")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {mensaje}\n")

def main():
    if len(sys.argv) != 3:
        print("Uso: python script.py <moneda> <umbral>")
        sys.exit(1)

    moneda = sys.argv[1].upper()
    umbral = float(sys.argv[2])
    precio = obtener_precio_binance(moneda)

    if precio is None:
        print("No se pudo obtener el precio.")
        sys.exit(1)
    
    if precio < umbral:
        mensaje = f"⚠️ Alerta: {moneda} ha caído por debajo del umbral de {umbral}. Precio actual: {precio}"
        enviar_alerta(mensaje)
        print("Alerta enviada.")
    else:
        guardar_log(f"{moneda} está por encima del umbral. Precio actual: {precio}")
        #print(f"{moneda} está por encima del umbral. Precio actual: {precio}")

if __name__ == "__main__":
    main()

