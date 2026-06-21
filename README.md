# Proyecto de Automatización QA - Prueba Técnica

**Autor:** Juan Felipe Muñoz Jimenez

Este repositorio contiene la resolución de la prueba técnica de automatización, abarcando pruebas de backend (API), pruebas móviles (UI) utilizando el patrón Page Object Model (POM), y un reto adicional de validación de telemetría de eventos con Kafka.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3
* **Framework de Pruebas:** Pytest
* **Pruebas Móviles:** Appium (Android)
* **Eventos/Telemetría:** Apache Kafka (Docker)
* **Control de Versiones:** Git / GitHub

## 📂 Estructura del Proyecto
```text
PROYECTO QA/
├── api-tests/              # Pruebas automatizadas de API REST
│   ├── config/             # Archivos de configuración de la API
│   └── specs/              
│       └── test_api.py     # Scripts de prueba de la API
├── app/                    # Directorio de la APK de prueba
├── event-tests/            # Pruebas de telemetría (Bonus)
│   └── specs/
│       └── test_kafka.py   # Validaciones Productor/Consumidor de Kafka
├── mobile-tests/           # Pruebas automatizadas para la App de Android
│   ├── page-objects/       # Implementación del patrón Page Object Model (POM)
│   │   └── login_page.py
│   └── specs/              
│       └── test_login.py   # Scripts de pruebas móviles
├── docker-compose.yml      # Configuración del broker local de Kafka
├── requirements.txt        # Dependencias del proyecto
├── README.md               # Documentación principal
└── AI_USAGE.md             # Declaración de uso de Inteligencia Artificial
```

## ⚙️ Configuración del Entorno

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Darchblack502/Proyecto-QA](https://github.com/Darchblack502/Proyecto-QA)
   cd "Proyecto-QA"
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Ejecución de Pruebas

### 1. Pruebas de API
Para ejecutar exclusivamente los scripts que validan los endpoints y las respuestas HTTP:
```bash
python -m pytest api-tests/ -v
```

### 2. Pruebas Móviles (Android)
**Requisitos previos:** * Tener un emulador de Android activo o dispositivo físico conectado (con las opciones de desarrollador habilitadas).
* Tener Appium Server ejecutándose en el puerto `4723`.

```bash
python -m pytest mobile-tests/ -v
```

### 3. Pruebas de Telemetría con Kafka (Bonus)
Se implementó la validación del flujo de telemetría simulando el envío y recepción de coordenadas de un vehículo. Para esto, se levanta un servidor Kafka en local.

**Requisitos previos:** * Tener Docker Desktop instalado y ejecutándose.

**Pasos de ejecución:**
1. Levantar la infraestructura local en segundo plano:
   ```bash
   docker compose up -d
   ```
2. Ejecutar la prueba de validación de contrato de eventos:
   ```bash
   python -m pytest event-tests/specs/test_kafka.py -v
   ```

### 4. Ejecución Total (Suite Completa)
Para ejecutar todas las pruebas del proyecto simultáneamente (API, Mobile y Eventos):
```bash
python -m pytest -v
```