import time
import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from data import message_for_driver


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


# Clase para agregar direccion desde y hasta
class UrbanRoutesPage:

    # Localizadores
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Acciones
    def set_from(self, address_from):
        self.driver.find_element(*self.from_field).send_keys(address_from)

    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def return_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def return_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_rout(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

# Seleccion del modo de viaje
class ComfortMethod:

    button_comfort = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]') # click()

    def __init__(self, driver):
        self.driver=driver

    def select_comfort(self):
        self.driver.find_element(*self.button_comfort).click()

    def return_status_trip(self):
        return self.driver.find_element(*self.button_comfort).is_displayed()

# Clase para rellenar el numero telefonico
class AddPhoneNumber:

    phone_number_holder = (By.ID, 'phone') # send_keys()
    button_phone_next = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button') # click()

    def __init__(self, driver):
        self.driver=driver

    def set_phon_number(self,number):
        self.driver.find_element(*self.phone_number_holder).send_keys(data.phone_number)

    def next_button_phone(self):
        self.driver.find_element(*self.button_phone_next).click()

    def return_phon_number(self):
        return self.driver.find_element(*self.phone_number_holder).get_property('value')

    def sent_phone_nomber(self,phone_number):
        self.set_phon_number(phone_number)
        self.next_button_phone()


# Mensaje para el conductor
class SendMessage:

    message_for_driver_holder = (By.CSS_SELECTOR, '#comment') # send_keys()

    def __init__(self,driver):
        self.driver=driver

    def set_message(self,message_for_driver):
        self.driver.find_element(*self.message_for_driver_holder).send_keys(message_for_driver)

    def return_message(self):
        return self.driver.find_element(*self.message_for_driver_holder).get_property('value')

#Clase para seleccionar manta y pañuelo
class BlanketHankySlider:

    blanket_hanky_slider = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span') # click()

    def __init__(self,driver):
        self.driver=driver

    def ask_blanket(self):
        self.driver.find_element(*self.blanket_hanky_slider).click()

    def return_displayed_blanket(self):
        return self.driver.find_element(*self.blanket_hanky_slider).is_displayed()

class TestUrbanRoutes:
    driver=None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    # 1 - Configurar la direccion
    def test_set_a_route(self):
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"from")))
        route_page = UrbanRoutesPage(self.driver)
        addres_from = data.address_from
        addres_to = data.address_to
        route_page.set_rout(addres_from, addres_to)
        assert route_page.return_from() == addres_from
        assert route_page.return_to() == addres_to

    # 2 - Seleccionar la tarifa Comfort
    def test_select_comfort(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,".//div[@class='results-text']/button[@class='button round']")))
        self.driver.find_element(By.XPATH,".//div[@class='results-text']/button[@class='button round']").click()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,".//*[text()='Comfort']")))
        travel_method = ComfortMethod(self.driver)
        travel_method.select_comfort()
        WebDriverWait(self.driver,10)
        assert travel_method.return_status_trip() == True

    # 3 - Rellenar el número de teléfono
    def test_select_phone_number(self):
        self.driver.find_element(By.CLASS_NAME,"np-text").click()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"phone")))
        send_new_phone = AddPhoneNumber(self.driver)
        new_phone = data.phone_number
        send_new_phone.sent_phone_nomber(new_phone)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"code")))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "code")))
        self.driver.find_element(By.ID, "code").send_keys(retrieve_phone_code(driver=self.driver))
        self.driver.find_element(By.XPATH, ".//*[text()='Confirmar']").click()
        assert send_new_phone.return_phon_number() == new_phone

    # 4 - Agregar una tarjeta de crédito
    def test_add_car(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,".//div[@class='pp-button filled']")))
        self.driver.find_element(By.XPATH,".//div[@class='pp-button filled']").click()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,".//img[@src='/static/media/card.411e0152.svg']")))
        self.driver.find_element(By.XPATH,".//img[@src='/static/media/card.411e0152.svg']").click()
        WebDriverWait(self.driver,10)
        number_card = data.card_number
        number_cvv = data.card_code
        self.driver.find_element(By.ID,"number").send_keys(number_card,Keys.TAB,number_cvv)
        return self.driver.find_element(By.ID,"number").get_property('value')
        assert self.driver.find_element(By.ID,"number") == number_card

    def test_quit_card_modal(self):
        return self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/button').click() # click()

    # 5 - Escribir un mensaje para el conductor
    def test_set_message(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "comment")))
        message = data.message_for_driver
        set_message = SendMessage(self.driver)
        set_message.set_message(message)
        assert set_message.return_message() == message

    # 6 - Pedir una manta y pañuelos
    def test_slider_blanket_hanky(self):
        return self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span').click()

    # 7 - Pedir 2 helados
    def test_1_ice_cream(self):
        return self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]').click()
        assert self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]') == '1'

    def test_2_ice_cream(self):
        return self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]').click()
        assert self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]') == '2'

    # 8 - Aparece el modal para buscar un taxi
    def test_pedir_taxi(self):
        time.sleep(4)
        return self.driver.find_element(By.CLASS_NAME, 'smart-button-main').click()
        assert self.driver.find_element(By.CSS_SELECTOR,"smart-button-secondary").is_enabled() == True


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()






