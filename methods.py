import data
import locators

# Clase para agregar direccion desde y hasta
class UrbanRoutesPage:

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Acciones
    def set_from(self, address_from):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.from_field).send_keys(address_from)

    def set_to(self, address_to):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.to_field).send_keys(address_to)

    def return_from(self):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.from_field).get_property('value')

    def return_to(self):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.to_field).get_property('value')

    def set_rout(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def select_comfort(self):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.button_comfort).click()

    def return_status_trip(self):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.button_comfort).is_displayed()

    def set_phon_number(self,number):
       return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.phone_number_holder).send_keys(data.phone_number)

    def next_button_phone(self):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.button_phone_next).click()

    def return_phon_number(self):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.phone_number_holder).get_property('value')

    def sent_phone_nomber(self,phone_number):
        self.set_phon_number(phone_number)
        self.next_button_phone()

    def set_message(self,message_for_driver):
        return (self.driver.find_element(*locators.LocatorsUrbanRoutesPage.message_for_driver_holder)
         .send_keys(message_for_driver))

    def return_message(self):
        return (self.driver.find_element(*locators.LocatorsUrbanRoutesPage.message_for_driver_holder)
                .get_property('value'))

    def ask_blanket(self):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.blanket_hanky_slider).click()

    def return_displayed_blanket(self):
        return self.driver.find_element(*locators.LocatorsUrbanRoutesPage.blanket_hanky_slider).is_displayed()