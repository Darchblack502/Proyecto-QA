import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

# Importamos nuestro Page Object
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'page-objects'))
from login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    # 1. Configuración de conexión con tu celular
    # NOTA: Cambia el nombre del archivo .apk si el tuyo se llama distinto
    ruta_app = os.path.join(os.getcwd(), "app", "Android-MyDemoAppRN.1.3.0.build-244.apk") 
    
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.automation_name = 'UiAutomator2'
    options.app = ruta_app
    options.auto_grant_permissions = True # Acepta permisos de Android automáticamente
    
    # Conexión al servidor de Appium (que debe estar corriendo en otra terminal)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    yield driver
    
    # 4. Limpieza: Cerramos la app al finalizar
    driver.quit()

def test_login_invalido(driver):
    # Inicializamos la página enviándole el control del celular
    login_page = LoginPage(driver)
    
    # Ejecutamos el flujo
    login_page.ir_a_login()
    login_page.hacer_login("juan_qa", "clave_equivocada")
    
    # Aserción: Validamos el manejo de credenciales inválidas
    error_texto = login_page.obtener_mensaje_error()
    assert "Provided credentials do not match" in error_texto, "El mensaje de error de login fallido no es el esperado"