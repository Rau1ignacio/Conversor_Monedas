
## API : https://api.exchangerate.host/convert?from=USD&to=EUR&amount=100

import requests # Importa la librería requests para hacer peticiones HTTP

def convertir_moneda(cantidad, de_moneda, a_moneda):
    url = f"https://api.exchangerate.host/convert?from={de_moneda}&to={a_moneda}&amount={cantidad}"

    response = requests.get(url)  # Realiza una petición GET a la API
    data = response.json()  # Convierte la respuesta a formato JSON

    if data['success']:
        resultado = data['result']
        print(f"{cantidad} {de_moneda} = {resultado:.2f} {a_moneda}")
    else:
        print("Error al obtener la conversión de moneda.")

if __name__ == "__main__":
    print("\n ============== Conversor de Monedas ==============")

    print("\nBienvenido al conversor de monedas.")
          
    cantidad = float(input("Ingrese la cantidad a convertir: "))
    de_moneda = input("Ingrese la moneda de origen (ej. USD): ").upper()
    a_moneda = input("Ingrese la moneda de destino (ej. EUR): ").upper()

    convertir_moneda(cantidad, de_moneda, a_moneda)

## Revisar como convertir mas monedas a la vez y errores que tengo en el codigo  