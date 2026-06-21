from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Espera dinámica explícita de hasta 10 segundos
        self.wait = WebDriverWait(driver, 10)

    # 1. SELECTORES (Usamos accessibility_id para evitar flakiness, como exige la prueba)
    MENU_HAMBURGUESA = (AppiumBy.ACCESSIBILITY_ID, "open menu")
    OPCION_LOGIN_MENU = (AppiumBy.ACCESSIBILITY_ID, "menu item log in")
    CAMPO_USUARIO = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
    CAMPO_PASSWORD = (AppiumBy.ACCESSIBILITY_ID, "Password input field")
    BOTON_LOGIN = (AppiumBy.ACCESSIBILITY_ID, "Login button")
    
    # Usamos XPath solo cuando no hay accessibility_id (para el mensaje de error)
    MENSAJE_ERROR = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Provided credentials do not match')]")

    # 2. ACCIONES DE NEGOCIO
    def ir_a_login(self):
        self.wait.until(EC.element_to_be_clickable(self.MENU_HAMBURGUESA)).click()
        self.wait.until(EC.element_to_be_clickable(self.OPCION_LOGIN_MENU)).click()

    def hacer_login(self, usuario, password):
        self.wait.until(EC.visibility_of_element_located(self.CAMPO_USUARIO)).send_keys(usuario)
        self.driver.find_element(*self.CAMPO_PASSWORD).send_keys(password)
        self.driver.find_element(*self.BOTON_LOGIN).click()

    def obtener_mensaje_error(self):
        return self.wait.until(EC.visibility_of_element_located(self.MENSAJE_ERROR)).text