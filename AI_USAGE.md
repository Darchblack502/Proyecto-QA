# Declaración de Uso de Inteligencia Artificial (AI Usage)

**Autor:** Juan Felipe Muñoz Jimenez

En cumplimiento con las buenas prácticas de desarrollo y los lineamientos de esta prueba técnica, detallo a continuación el uso de Inteligencias Artificiales (específicamente Gemini) como herramienta de apoyo durante la construcción de este proyecto.

## Áreas de Aplicación de la IA

1. **Estructura y Arquitectura del Proyecto (POM):**
   * Se consultó a la IA para definir la mejor estructura de carpetas en Python utilizando Pytest.
   * Se utilizó apoyo conceptual para implementar correctamente el patrón de diseño **Page Object Model (POM)** en la capa de pruebas móviles con Appium, asegurando la separación de los localizadores de la lógica de negocio.

2. **Soporte Técnico y Depuración (Debugging):**
   * La IA fue utilizada como asistente para resolver errores de sintaxis y excepciones específicas de las librerías `pytest` y `appium-python-client`.
   * Se validaron estrategias para la correcta identificación de selectores móviles y tiempos de espera explícitos (Waits).

3. **Infraestructura y Resolución de Entornos (Bonus de Kafka):**
   * Se utilizó la IA para solucionar problemas de configuración de entornos en Windows, específicamente resolviendo bloqueos en la activación del Subsistema de Windows para Linux (WSL) requerido por Docker.
   * La IA proporcionó el archivo `docker-compose.yml` utilizando la imagen oficial de Apache Kafka, agilizando el levantamiento del broker local necesario para validar el contrato de datos entre Productor y Consumidor.

4. **Documentación:**
   * Apoyo en la redacción y formateo del archivo `README.md` utilizando sintaxis Markdown para garantizar una presentación clara, profesional y fácil de seguir para los evaluadores.

## Conclusión

El uso de la Inteligencia Artificial se limitó a actuar como un par consultor y soporte de infraestructura. Toda la lógica de aserciones, el diseño de los casos de prueba, y la ejecución final fueron verificados, adaptados y ejecutados manualmente para garantizar el cumplimiento estricto de los requerimientos técnicos solicitados.