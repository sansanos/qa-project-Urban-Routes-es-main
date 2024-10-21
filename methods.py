from selenium.webdriver.ie.webdriver import WebDriver
import data
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:
    from_field = locators.LocatorsUrbanRoutesPage.from_field
    to_field = locators.LocatorsUrbanRoutesPage.to_field
    button_round = locators.LocatorsUrbanRoutesPage.button_round
    button_comfort = locators.LocatorsUrbanRoutesPage.button_comfort
    button_phone_number = locators.LocatorsUrbanRoutesPage.button_phone_number
    phone_number_holder = locators.LocatorsUrbanRoutesPage.phone_number_holder
    button_phone_next = locators.LocatorsUrbanRoutesPage.button_phone_next
    sms_code_holder = locators.LocatorsUrbanRoutesPage.sms_code_holder
    button_sms_code_confirmation = locators.LocatorsUrbanRoutesPage.button_sms_code_confirmation
    button_payment = locators.LocatorsUrbanRoutesPage.button_payment
    button_add_card = locators.LocatorsUrbanRoutesPage.button_add_card
    card_number_holder = locators.LocatorsUrbanRoutesPage.card_number_holder
    card_code_holder = locators.LocatorsUrbanRoutesPage.card_code_holder
    click_code_holder = locators.LocatorsUrbanRoutesPage.click_code_holder
    add_card_confirmation = locators.LocatorsUrbanRoutesPage.add_card_confirmation
    card_quit = locators.LocatorsUrbanRoutesPage.card_quit
    message_for_driver_holder = locators.LocatorsUrbanRoutesPage.message_for_driver_holder
    manta_panuelo_slider = locators.LocatorsUrbanRoutesPage.manta_panuelo_slider
    helado_plus = locators.LocatorsUrbanRoutesPage.helado_plus
    helado_counter = locators.LocatorsUrbanRoutesPage.helado_counter
    smart_button_main = locators.LocatorsUrbanRoutesPage.smart_button_main
    modal_window = locators.LocatorsUrbanRoutesPage.modal_window
    modal_order_header_title = locators.LocatorsUrbanRoutesPage.modal_order_header_title
    modal_window_driver = locators.LocatorsUrbanRoutesPage.modal_window_driver

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.from_field))

    def set_from(self, address_from):
        self.driver.find_element(*self.from_field).send_keys(address_from)

    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def button_round_click(self):
        return self.driver.find_element(*self.button_round).click()

    def button_comfort_click(self):
        return self.driver.find_element(*self.button_comfort).click()

    def wait_for_comfort_options(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(*self.manta_panuelo_slider))

    def get_button_comfort_click_text(self):
        return self.driver.find_element(*self.button_comfort).text

    def button_phone_number_click(self):
        return self.driver.find_element(*self.button_phone_number).click()

    def phone_number_holder_set(self, phone_number):
        return self.driver.find_element(*self.phone_number_holder).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_holder).get_property('value')

    def button_phone_next_click(self):
        return self.driver.find_element(*self.button_phone_next).click()

    def sms_code_holder_set(self, code):
        return self.driver.find_element(*self.sms_code_holder).send_keys(code)

    def get_sms_code(self):
        return self.driver.find_element(*self.sms_code_holder).get_property('value')

    def button_sms_code_confirmation_click(self):
        return self.driver.find_element(*self.button_sms_code_confirmation).click()

    def button_payment_click(self):
        return self.driver.find_element(*self.button_payment).click()

    def button_add_card_click(self):
        return self.driver.find_element(*self.button_add_card).click()

    def card_number_holder_set(self, card_number):
        return self.driver.find_element(*self.card_number_holder).send_keys(card_number)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number_holder).get_property('value')

    def card_code_holder_set(self, card_code):
        return self.driver.find_element(*self.card_code_holder).send_keys(card_code)

    def get_card_code(self):
        return self.driver.find_element(*self.card_code_holder).get_property('value')

    def click_code_holder_click(self):
        return self.driver.find_element(*self.click_code_holder).click()

    def add_card_confirmation_click(self):
        return self.driver.find_element(*self.add_card_confirmation).click()

    def card_quit_click(self):
        return self.driver.find_element(*self.card_quit).click()

    def message_for_driver_holder_set(self, message_for_driver):
        return self.driver.find_element(*self.message_for_driver_holder).send_keys(message_for_driver)

    def get_driver_message_text(self):
        return self.driver.find_element(*self.message_for_driver_holder).text

    def manta_panuelo_slider_click(self):
        return self.driver.find_element(*self.manta_panuelo_slider).click

    def helado_plus_click(self):
        return self.driver.find_element(*self.helado_plus).click()

    def get_helado_counter(self):
        return self.driver.find_element(*self.helado_counter).text

    def smart_button_main_click(self):
        return self.driver.find_element(*self.smart_button_main).click

    def wait_for_load_modal(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(*self.modal_window))

    def get_modal_window_text(self):
        return self.driver.find_element(*self.modal_order_header_title).text

    def wait_for_load_modal_driver_info(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(*self.modal_window_driver))






