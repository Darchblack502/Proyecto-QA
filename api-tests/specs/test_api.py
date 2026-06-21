import requests
import time
from jsonschema import validate

def test_crear_reserva_exitosa():
    # 1. PREPARACIÓN (Arrange)
    url = "https://restful-booker.herokuapp.com/booking"
    
    # Creamos un payload dinámico generando un precio aleatorio basado en el tiempo.
    # Cumple con el requisito: "Peticiones Mutables (POST/PUT): Envio de payloads dinámicos en formato JSON"
    payload = {
        "firstname" : "Juan Felipe",
        "lastname" : "Muñoz Jimenez",
        "totalprice" : int(time.time() % 1000), 
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2026-07-01",
            "checkout" : "2026-07-15"
        },
        "additionalneeds" : "Desayuno"
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Definimos el JSON Schema que esperamos recibir de vuelta.
    # Cumple con el requisito de "Validación de Contrato (JSON Schema)"
    schema_esperado = {
        "type": "object",
        "properties": {
            "bookingid": {"type": "integer"},
            "booking": {
                "type": "object",
                "properties": {
                    "firstname": {"type": "string"},
                    "lastname": {"type": "string"}
                },
                "required": ["firstname", "lastname"]
            }
        },
        "required": ["bookingid", "booking"]
    }

    # 2. ACCIÓN (Act)
    # Ejecutamos la petición POST
    response = requests.post(url, json=payload, headers=headers)

    # 3. ASERCIONES (Assert)
    
    # A. Aserciones de Estado [cite: 62]
    assert response.status_code == 200, f"Error: Código de estado esperado 200, pero se recibió {response.status_code}"
    assert "application/json" in response.headers.get("Content-Type", ""), "Error: La cabecera Content-Type no es JSON"
    
    # B. SLA de Rendimiento 
    tiempo_respuesta = response.elapsed.total_seconds()
    assert tiempo_respuesta < 1.5, f"SLA fallido: La respuesta tardó {tiempo_respuesta} segundos, superando el límite de 1.5s"

    # C. Validación de Contrato (JSON Schema) 
    data = response.json()
    validate(instance=data, schema=schema_esperado) # Si el esquema no coincide, pytest fallará automáticamente

    print("\n--- RESPUESTA DE LA API ---")
    print(response.json())
    print("---------------------------\n")