# Urban Routes – Pruebas Automatizadas de Interfaz Web

## Descripción
Este proyecto contiene pruebas automatizadas diseñadas para validar el correcto funcionamiento de la página web **Urban Routes**, mediante la simulación de acciones reales de usuario.  
El objetivo del proyecto es garantizar la estabilidad y usabilidad del sistema web, aplicando buenas prácticas de automatización y aseguramiento de calidad.

## Tecnologías y Herramientas
- Python 3.13  
- Selenium WebDriver 4.34.2  
- Pytest 8.4.1  
- PyCharm 2025.1.3  
- Control de versiones con Git/GitHub  

## Escenarios Automatizados
Las pruebas cubren la automatización de las siguientes acciones principales:
- Introducción de direcciones de origen y destino.  
- Selección de la tarifa **Comfort**.  
- Llenado del campo **número de teléfono**.  
- Registro de **tarjeta de crédito**.  
- Envío de **mensaje para el conductor**.  
- Activación de la opción **“Manta y pañuelos”**.  
- Ajuste de cantidad en **“Helados”** a 2 unidades.  
- Reserva final al hacer clic en **“Reservar”** tras completar los campos obligatorios.  

## Técnicas y Estructura
- **Estructura modular:** Separación de pruebas, datos y funciones auxiliares para una mejor organización y mantenibilidad.  
- **Page Object Model (POM):** Diseño orientado a reutilización y reducción de redundancia en el código.  
- **Sincronización dinámica:** Uso de `WebDriverWait` y `expected_conditions` para interactuar correctamente con los elementos de la interfaz.  
- **Localización de elementos:** Estrategias mediante `ID`, `CSS_SELECTOR` y `XPATH`.  
- **Simulación de usuario:** Implementación de `send_keys` y `Keys.TAB` para emular entradas reales.  

## Prerrequisitos
1. Tener instalado **Python 3.13**.  
2. Instalar los paquetes necesarios ejecutando:  
   ```sh
   pip install selenium pytest
   ```
   
## Ejecución de Pruebas   
1. Clona el repositorio
  ```sh
   git clone https://github.com/Kevsql/Urban_Routes_Automated_tests.git
   ```
2. Configura la variable `urban_routes_url` en `data.py` con la URL del servidor.
3. Ejecuta las pruebas desde el archivo `test_urban_routes.py`
