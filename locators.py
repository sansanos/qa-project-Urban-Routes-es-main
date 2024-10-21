from selenium.webdriver.common.by import By

class LocatorsUrbanRoutesPage:

    from_field = (By.ID, 'from') # send_keys()
    to_field = (By.ID, 'to') # send_keys()
    button_round = (By.CLASS_NAME, 'button round') # click()
    button_comfort = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]') # click()
    button_phone_number = (By.CLASS_NAME, 'np-text') # click()
    phone_number_holder = (By.ID, 'phone') # send_keys()
    button_phone_next = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button') # click()
    sms_code_holder = (By.XPATH, '//*[@id="code"]') # send_keys()
    button_sms_code_confirmation = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]') # click()
    button_payment = (By.CLASS_NAME, 'pp-button filled') # click()
    button_add_card = (By.CLASS_NAME, 'pp-row disabled') # click()
    card_number_holder = (By.CLASS_NAME, 'card-number-input') # send_keys()
    card_code_holder = (By.CLASS_NAME, 'card-code-input') # send_keys()
    click_code_holder = (By.CLASS_NAME, 'payment-picker open') # click()
    add_card_confirmation = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]') # click()
    card_quit = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/button') # click()
    message_for_driver_holder = (By.ID, 'comment') # send_keys()
    manta_panuelo_slider = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span') # click()
    helado_plus = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]') # click() x2
    helado_counter = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]') # text
    smart_button_main = (By.CLASS_NAME, 'smart-button-main') # click()
    modal_window = (By.CLASS_NAME, 'order-body') # wait

