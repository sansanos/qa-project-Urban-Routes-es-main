import time
import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


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


#Clase de seccion para agregar direccion desde y hasta
class UrbanRoutesPage:
    #Indicar Marcadores
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    #Generar constructor
    def __init__(self, driver):
        self.driver = driver

    #Generar Accion
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def return_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def return_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_rout(self,from_address,to_address):
        self.set_from(from_address)
        self.set_to(to_address)

#Seleccionar modo de viaje
class ComfortMethod:
    comfort_button=(By.XPATH,".//*[text()='Comfort']" )
    def __init__(self,driver):
        self.driver=driver
    def select_comfort(self):
        self.driver.find_element(*self.comfort_button).click()
    def return_status_trip(self):
        return self.driver.find_element(*self.comfort_button).is_displayed()

#Clase para seccion de llenado de numero telefonico
class AddPhoneNumber:
    place_to_phone_nomber=(By.ID,"phone")
    next_button=(By.XPATH,".//div[@class='buttons']/button[@class='button full']")

    def __init__(self,driver):
        self.driver=driver

    def whrite_phon_number(self,number):
        self.driver.find_element(*self.place_to_phone_nomber).send_keys(number)

    def post_number(self):
        self.driver.find_element(*self.next_button).click()

    def return_phon_number(self):
        return self.driver.find_element(*self.place_to_phone_nomber).get_property('value')
    def sent_phone_nomber(self,number):
        self.whrite_phon_number(number)
        self.post_number()


#Clase para colocar un nuevo mensaje para el conductor
class SendNewMessage:
    coment_space=(By.CSS_SELECTOR,"#comment")
    def __init__(self,driver):
        self.driver=driver
    def white_mew_message(self,message):
        self.driver.find_element(*self.coment_space).send_keys(message)
    def return_message(self):
        return self.driver.find_element(*self.coment_space).get_property('value')

#Clase para validar solicitud de manta y pañuelo
class AskBlanket:
    ask_blanket_button=(By.XPATH,"//div[@class='r-sw-container']/div[@class='r-sw']/div[@class='switch']")
    def __init__(self,driver):
        self.driver=driver
    def ask_blanket(self):
        self.driver.find_element(*self.ask_blanket_button).click()
    def return_estatus_blanket(self):
        return self.driver.find_element(*self.ask_blanket_button).is_displayed()

class TestUrbanRoutes:
    driver=None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    #Prueba para validar el alta de datos origen y destino
    def test_set_a_route(self):
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"from")))
        route_page=UrbanRoutesPage(self.driver)
        addres_from = data.address_from
        addres_to= data.address_to
        route_page.set_rout(addres_from,addres_to)
        assert route_page.return_from()==addres_from
        assert route_page.return_to()==addres_to

    #Prueba 2 Validar la seleccion de metodo de traslado comfort
    def test_select_comfort(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,".//div[@class='results-text']/button[@class='button round']")))
        self.driver.find_element(By.XPATH,".//div[@class='results-text']/button[@class='button round']").click()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,".//*[text()='Comfort']")))
        travel_method=ComfortMethod(self.driver)
        travel_method.select_comfort()
        WebDriverWait(self.driver,10)
        assert travel_method.return_status_trip()==True

    #Prueba 3 Comprobar el llenado de numero telefonico
    def test_select_phone_number(self):
        self.driver.find_element(By.CLASS_NAME,"np-text").click()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"phone")))
        send_new_phone=AddPhoneNumber(self.driver)
        new_phone=data.phone_number
        send_new_phone.sent_phone_nomber(new_phone)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"code")))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "code")))
        self.driver.find_element(By.ID, "code").send_keys(retrieve_phone_code(driver=self.driver))
        self.driver.find_element(By.XPATH, ".//*[text()='Confirmar']").click()
        assert send_new_phone.return_phon_number() == new_phone

    def test_add_credit_car_part_1(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,".//div[@class='pp-button filled']")))
        self.driver.find_element(By.XPATH,".//div[@class='pp-button filled']").click()
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,".//img[@src='/static/media/card.411e0152.svg']")))
        self.driver.find_element(By.XPATH,".//img[@src='/static/media/card.411e0152.svg']").click()
        WebDriverWait(self.driver,10)
        number_card=data.card_number
        number_cvv=data.card_code
        self.driver.find_element(By.ID,"number").send_keys(number_card,Keys.TAB,number_cvv)
        return self.driver.find_element(By.ID,"number").get_property('value')
        assert self.driver.find_element(By.ID,"number")==number_card

        time.sleep(4)


    #Prueba 5 escribir un mensaje para el controlador
    def test_whrite_message(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"comment")))
        message=data.message_for_driver
        whrite_message=SendNewMessage(self.driver)
        whrite_message.white_mew_message(message)
        assert whrite_message.return_message()==message


    #Prueba 6 Pedir una manta y pañuelo
    def test_ask_for_blanket(self):
        self.driver.find_element(By.ID,"comment").send_keys(Keys.TAB,Keys.SPACE)
        assert self.driver.find_element(By.XPATH,"//div[@class='r-sw-container']/div[@class='r-sw']/div[@class='switch']").is_enabled()


    #Prueba 7 solicitar 2 helados
    def test_2_icecream(self):
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]').click()
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]').click()
        assert self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]') == '2'
    #Prueba 8
    def test_final_button(self):
        assert self.driver.find_element(By.CSS_SELECTOR,"smart-button-secondary").is_enabled() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()






