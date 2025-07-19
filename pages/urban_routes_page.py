from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:
    #Localizadores test 1
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    #Localizadores test 2
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_rate = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    tcard_change = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[@class='tcard-title' and text()='Comfort']]")

    #Localizadores test 3
    phone_number_button = (By.CSS_SELECTOR, '.np-button')
    phone_number_text = (By.ID, 'phone')
    submit_phone_number_window = (By.CSS_SELECTOR, '.buttons')
    phone_number_code_location = (By.ID, 'code')
    finish_phone_number_fill = (By.XPATH, "//div[@class='buttons']//button[text()='Confirmar']")
    phone_number_assert = (By.CSS_SELECTOR, '.np-text')

    #Localizadores test 4
    payment_method_button = (By.CSS_SELECTOR, '.pp-button')
    add_card_button = (By.CSS_SELECTOR, '.pp-row.disabled')
    add_card_number = (By.ID, 'number')
    add_card_code = (By.XPATH, "//div[@class='card-code-input']/input")
    submit_card = (By.XPATH, "//div[@class='pp-buttons']//button[text()='Agregar']")
    close_card_window = (By.CSS_SELECTOR, "div.payment-picker.open div.modal button.close-button.section-close")
    payment_method_assert = (By.XPATH, "//div[@class='pp-value-text' and text()='Tarjeta']")

    #Localizadores test 5
    driver_message_field = (By.CSS_SELECTOR, "div.form div.input-container input.input")

    #Localizadores test 6
    request_blanket_and_handkerchiefs = (By.XPATH, '//div[text()="Manta y pañuelos"]/following::span[@class="slider round"][1]')
    assert_request_blanket_and_handkerchiefs = (By.XPATH, '//div[text()="Manta y pañuelos"]/following::input[@type="checkbox" and contains(@class,"switch-input")][1]')

    #Localizadores test 7
    request_ice_cream = (By.XPATH, '//div[@class="r-counter-label" and text()="Helado"]/following-sibling::div[@class="r-counter"]//div[@class="counter-plus"]')
    request_ice_cream_value = (By.XPATH, '//div[@class="r-counter-label" and text()="Helado"]/following-sibling::div[@class="r-counter"]//div[@class="counter-value"]')

    #Localizadores test 8
    request_trip = (By.CSS_SELECTOR, 'button.smart-button')
    trip_confirmed = (By.CSS_SELECTOR, '.order.shown')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    #test 1 métodos
    def set_from(self, from_address):
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    #test 2 métodos
    def get_request_taxi_button(self):
        return self.wait.until(EC.presence_of_element_located(self.request_taxi_button))

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_rate_icon(self):
        return self.wait.until(EC.presence_of_element_located(self.comfort_rate))

    def click_comfort_rate_icon(self):
        self.get_comfort_rate_icon().click()

    def get_tcard_change(self):
        return self.wait.until(EC.presence_of_element_located(self.tcard_change))

    #test 3 métodos
    def get_phone_number_button(self):
        return self.wait.until(EC.presence_of_element_located(self.phone_number_button))

    def click_phone_number_button(self):
        self.get_phone_number_button().click()

    def set_phone_number(self, number_phone):
        self.wait.until(EC.presence_of_element_located(self.phone_number_text)).send_keys(number_phone)

    def get_submit_phone_number_window(self):
        return self.wait.until(EC.presence_of_element_located(self.submit_phone_number_window))

    def click_submit_phone_number(self):
        self.get_submit_phone_number_window().click()

    def set_phone_number_code(self, phone_code):
        self.wait.until(EC.presence_of_element_located(self.phone_number_code_location)).send_keys(phone_code)

    def get_finish_fill_phone_number(self):
        return self.wait.until(EC.presence_of_element_located(self.finish_phone_number_fill))

    def click_finish_fill_phone_number(self):
        self.get_finish_fill_phone_number().click()

    def get_phone_number_assert(self):
        return self.driver.find_element(*self.phone_number_assert).text

    #test 4 métodos
    def get_payment_method_button(self):
        return self.wait.until(EC.presence_of_element_located(self.payment_method_button))

    def click_payment_method_button(self):
        self.get_payment_method_button().click()

    def get_add_card_button(self):
        return self.wait.until(EC.presence_of_element_located(self.add_card_button))

    def click_add_card_button(self):
        self.get_add_card_button().click()

    def set_add_card_number(self, card_number):
        self.wait.until(EC.element_to_be_clickable(self.add_card_number)).send_keys(card_number + Keys.TAB)

    def set_add_card_code(self, card_code):
        self.wait.until(EC.element_to_be_clickable(self.add_card_code)).send_keys(card_code + Keys.TAB)

    def get_submit_card(self):
        return self.wait.until(EC.presence_of_element_located(self.submit_card))

    def click_submit_card(self):
        self.get_submit_card().click()

    def get_close_card_window(self):
        return self.wait.until(EC.element_to_be_clickable(self.close_card_window))

    def click_close_card_window(self):
        self.get_close_card_window().click()

    def get_payment_method_assert(self):
        return self.driver.find_element(*self.payment_method_assert).text

    #test 5 métodos
    def write_driver_message_field(self, message_for_driver):
        self.wait.until(EC.presence_of_element_located(self.driver_message_field)).send_keys(message_for_driver + Keys.TAB)

    def get_driver_message_field(self):
        return self.driver.find_element(*self.driver_message_field).get_property('value')

    #test 6 métodos
    def get_request_blanket_and_handkerchiefs(self):
        return self.wait.until(EC.element_to_be_clickable(self.request_blanket_and_handkerchiefs))

    def click_request_blanket_and_handkerchiefs(self):
        self.get_request_blanket_and_handkerchiefs().click()

    def get_assert_request_blanket_and_handkerchiefs(self):
        return self.driver.find_element(*self.assert_request_blanket_and_handkerchiefs).is_selected()

    #test 7 métodos
    def get_request_ice_cream(self):
        return self.wait.until(EC.element_to_be_clickable(self.request_ice_cream))

    def click_request_ice_cream(self):
        self.get_request_ice_cream().click()

    def get_request_ice_cream_value(self):
        return self.driver.find_element(*self.request_ice_cream_value).text

    #test 8 métodos
    def get_request_trip(self):
        return self.wait.until(EC.element_to_be_clickable(self.request_trip))

    def click_request_trip(self):
        self.get_request_trip().click()

    def get_trip_confirmed(self):
        return self.wait.until(EC.visibility_of_element_located(self.trip_confirmed))
