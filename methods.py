import data
import locators

# Clase para agregar direccion desde y hasta
class UrbanRoutesPage:

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Acciones
    def set_from(self, address_from):
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.from_field).send_keys(address_from)

    def set_to(self, address_to):
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.to_field).send_keys(address_to)

    def return_from(self):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.from_field).get_property('value')

    def return_to(self):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.to_field).get_property('value')

    def set_rout(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

# Seleccion del modo de viaje
class ComfortMethod:

    def __init__(self, driver):
        self.driver=driver

    def select_comfort(self):
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.button_comfort).click()

    def return_status_trip(self):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.button_comfort).is_displayed()

# Clase para rellenar el numero telefonico
class AddPhoneNumber:

    def __init__(self, driver):
        self.driver=driver

    def set_phon_number(self,number):
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.phone_number_holder).send_keys(data.phone_number)

    def next_button_phone(self):
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.button_phone_next).click()

    def return_phon_number(self):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.phone_number_holder).get_property('value')

    def sent_phone_nomber(self,phone_number):
        self.set_phon_number(phone_number)
        self.next_button_phone()

# Mensaje para el conductor
class SendMessage:

    def __init__(self,driver):
        self.driver=driver

    def set_message(self,message_for_driver):
        (self.driver.find_element(*locators.LocatorsUrbanRoutesPage.message_for_driver_holder)
         .send_keys(message_for_driver))

    def return_message(self):
        return (self.driver.find_element(*locators.LocatorsUrbanRoutesPage.message_for_driver_holder)
                .get_property('value'))

#Clase para seleccionar manta y pañuelo
class BlanketHankySlider:

    def __init__(self,driver):
        self.driver=driver

    def ask_blanket(self):
        self.driver.find_element(*locators.LocatorsUrbanRoutesPage.blanket_hanky_slider).click()

    def return_displayed_blanket(self):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.blanket_hanky_slider).is_displayed()