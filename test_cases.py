
import data
import locators
from data import address_from, address_to
from methods import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class TestUrbanRoutes:
    driver = None
    #methods = None

    def __init__(self, driver):
        self.driver = driver
        self.UrbanRoutesPage = data.urban_routes_url

    @classmethod
    def setup_class(cls):
        # Configurar las opciones del navegador
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        # Iniciar el servicio de Chrome
        service = Service()  # Puedes pasar el path del driver aquí si es necesario

        # Inicializar el driver con opciones
        cls.driver = webdriver.Chrome(service=service, options=options)

    # Configurar la direccion
    def test_set_route(self):
        self.UrbanRoutesPage.set_from()
        self.UrbanRoutesPage.set_to()
        assert self.UrbanRoutesPage.get_from() == data.address_from
        assert self.UrbanRoutesPage.get_to() == data.address_to

    # Seleccionar la tarifa
    def test_comfort_text(self):
        self.UrbanRoutesPage.button_comfort_click()
        assert self.UrbanRoutesPage.wait_for_comfort_options() == 400

    # Rellenar el numero de telefono
    def test_full_phone_number(self):
        self.UrbanRoutesPage.phone_number_holder_set()
        phone_number_value = self.UrbanRoutesPage.get_phone_number()
        assert phone_number_value == '+1 123 123 12 12'
        self.UrbanRoutesPage.button_phone_next_click()
        self.UrbanRoutesPage.sms_code_holder_set()
        self.UrbanRoutesPage.button_sms_code_confirmation_click()

    # Agregar tarjeta de credito
    def test_add_card(self):
        self.UrbanRoutesPage.button_payment_click()
        self.UrbanRoutesPage.button_add_card_click()
        self.UrbanRoutesPage.card_number_holder_set()
        self.UrbanRoutesPage.card_code_holder_set()
        assert self.UrbanRoutesPage.get_card_number() == '1234 5678 9100'
        assert self.UrbanRoutesPage.get_card_code() == '111'
        self.UrbanRoutesPage.click_code_holder_click()
        self.UrbanRoutesPage.add_card_confirmation_click()

    # Escribir un mensaje para el conductor
    def test_driver_message_text(self):
        self.UrbanRoutesPage.message_for_driver_holder_set()
        assert self.UrbanRoutesPage.get_driver_message_text() == 'Voy al museo'

    # Pedir una manta y panuelos
    def test_manta_panuelos_slider(self):
        self.UrbanRoutesPage.manta_panuelo_slider_click()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
