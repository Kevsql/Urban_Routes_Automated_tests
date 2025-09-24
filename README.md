# Proyecto Urban Grocers
Kevin Alvarado Salazar 

Pruebas automatizadas para comprobar la funcionalidad de la página web Urban Routes.

Tecnologías utilizadas:
- PyCharm (PyCharm 2025.1.3).
- Python (Versión 3.13).
- Selenium WebDriver (Versión 4.34.2).
- Pytest (Versión 8.4.1).
#
Técnicas utilizadas:
- Estructura modular de archivos para separar pruebas, datos y funciones especiales.
- Diseño de codigo usando Page Object Model (POM).
- WebDriverWait y expected_conditions para interactuar con los elementos adecuadamente.
- Localizadores HTML del tipo: ID, CSS_SELECTOR y XPATH.
- Simulación de entradas de usuario con send_keys y Keys.TAB
#
Ejecución de las pruebas:
- Tener instalados:
    - python
    - selenium
    - pytest
    - selenium
- Colocar la dirección URL del servidor en la variable 'urban_routes_url' localizada en data>data.py.
- Correr las pruebas desde el archivo 'test_urban_routes.py' localizado en la carpeta tests.
