import time
import code_sms
import data
import locators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from methods import UrbanRoutesPage, ComfortMethod, AddPhoneNumber, SendMessage


class TestUrbanRoutes:
    driver=None

    @classmethod
    def setup_class(cls):
        # no modificar, se necesita un registro para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    # 1 - Configurar la direccion
    def test_set_a_route(self):
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsUrbanRoutesPage.from_field))
        route_page = UrbanRoutesPage(self.driver)
        route_page.set_rout(data.address_from, data.address_to)
        assert route_page.return_from() == data.address_from
        assert route_page.return_to() == data.address_to

    # 2 - Seleccionar la tarifa Comfort
    def test_select_comfort(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsUrbanRoutesPage.button_round))
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.button_round).click()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsUrbanRoutesPage.button_comfort))
        travel_method = ComfortMethod(self.driver)
        travel_method.select_comfort()
        WebDriverWait(self.driver,10)
        assert travel_method.return_status_trip() == True

    # 3 - Rellenar el número de teléfono
    def test_select_phone_number(self):
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.button_phone_number).click()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsUrbanRoutesPage.phone_number_holder))
        send_new_phone = AddPhoneNumber(self.driver)
        send_new_phone.sent_phone_nomber(data.phone_number)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsUrbanRoutesPage.sms_code_holder))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsUrbanRoutesPage.sms_code_holder))
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.sms_code_holder).send_keys(
            code_sms.retrieve_phone_code(driver=self.driver))
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.button_sms_code_confirmation).click()
        assert send_new_phone.return_phon_number() == data.phone_number

    # 4 - Agregar una tarjeta de crédito
    def test_add_car(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsUrbanRoutesPage.button_payment))
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.button_payment).click()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsUrbanRoutesPage.button_payment_card))
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.button_payment_card).click()
        WebDriverWait(self.driver,10)
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.card_number_holder).send_keys(
            data.card_number,Keys.TAB,data.card_code)
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.card_number_holder).get_property('value')
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.card_quit).click()  # click()
        assert self.driver.find_element(*locators.LocatorsUrbanRoutesPage.card_quit).is_enabled() == True
        assert (self.driver.find_element(*locators.LocatorsUrbanRoutesPage.card_number_holder).get_property('value')
                == data.card_number)

    # 5 - Escribir un mensaje para el conductor
    def test_set_message(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsUrbanRoutesPage.message_for_driver_holder))
        set_message = SendMessage(self.driver)
        set_message.set_message(data.message_for_driver)
        assert set_message.return_message() == data.message_for_driver

    # 6 - Pedir una manta y pañuelos
    def test_slider_blanket_hanky(self):
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.blanket_hanky_slider).click()
        assert self.driver.find_element(*locators.LocatorsUrbanRoutesPage.blanket_hanky_slider).is_displayed()

    # 7 - Pedir 2 helados
    def test_ice_cream(self):
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.ice_cream_plus).click()
        assert self.driver.find_element(*locators.LocatorsUrbanRoutesPage.ice_cream_counter).text == '1'
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.ice_cream_plus).click()
        assert self.driver.find_element(*locators.LocatorsUrbanRoutesPage.ice_cream_counter).text == '2'

    # 8 - Aparece el modal para buscar un taxi
    def test_pedir_taxi(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            locators.LocatorsUrbanRoutesPage.smart_button_main_pedir_un_taxi))
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.smart_button_main_pedir_un_taxi).click()
        assert (self.driver.find_element(*locators.LocatorsUrbanRoutesPage.smart_button_main_pedir_un_taxi).is_enabled()
                == True)

    # 9 - Esperar a que aparezca la información del conductor en el modal
    def test_driver_modal_window(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(
            locators.LocatorsUrbanRoutesPage.modal_window_car_icon))
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.modal_order_header_title)
        assert (self.driver.find_element(*locators.LocatorsUrbanRoutesPage.modal_window_car_icon).get_property('alt')
                == 'Car')


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()






