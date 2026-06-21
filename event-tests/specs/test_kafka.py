import json
import pytest
from kafka import KafkaProducer, KafkaConsumer

# Configuración del servidor Kafka (La llenaremos en el paso 2)
KAFKA_BROKER = 'localhost:9092'
TOPIC_NAME = 'gps-raw-events'

def test_flujo_telemetria_kafka():
    # 1. PRODUCTOR: Enviar el mensaje de telemetría
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BROKER],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    # Payload exigido en la prueba
    payload = {
        "vehicleId": "VEH-99",
        "lat": 4.60,
        "lng": -74.08,
        "speed": 65
    }
    
    # Publicamos el JSON en el tópico
    producer.send(TOPIC_NAME, value=payload)
    producer.flush() # Forzamos el envío inmediato
    
    # 2. CONSUMIDOR: Leer el mensaje
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=[KAFKA_BROKER],
        auto_offset_reset='earliest', # Lee desde el principio
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        consumer_timeout_ms=5000 # Espera máximo 5 segundos para no quedarse colgado
    )
    
    mensaje_recibido = None
    for message in consumer:
        mensaje_recibido = message.value
        break # Leemos el primer mensaje y cerramos
        
    # 3. ASERCIONES: Validar recepción y estructura del contrato
    assert mensaje_recibido is not None, "El consumidor no recibió ningún mensaje."
    assert mensaje_recibido["vehicleId"] == "VEH-99", "El ID del vehículo no coincide."
    assert "lat" in mensaje_recibido and "lng" in mensaje_recibido, "Faltan las coordenadas GPS."
    assert isinstance(mensaje_recibido["speed"], int), "La velocidad debe ser un valor numérico entero."