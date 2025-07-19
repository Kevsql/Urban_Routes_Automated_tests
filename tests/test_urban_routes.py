from data import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages import urban_routes_page as urp
from utils import retrieve_code

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_select_comfort_rate(self):
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_rate_icon()
        assert "active" in self.routes_page.get_tcard_change().get_attribute("class")

    def test_fill_phone_number(self):
        self.routes_page.click_phone_number_button()
        phone_number = data.phone_number
        self.routes_page.set_phone_number(phone_number)
        self.routes_page.click_submit_phone_number()
        phone_code = retrieve_code.retrieve_phone_code(self.driver)
        self.routes_page.set_phone_number_code(phone_code)
        self.routes_page.click_finish_fill_phone_number()
        assert self.routes_page.get_phone_number_assert() == phone_number

    def test_add_card_as_payment_method(self):
        self.routes_page.click_payment_method_button()
        self.routes_page.click_add_card_button()
        card_number = data.card_number
        card_code = data.card_code
        self.routes_page.set_add_card_number(card_number)
        self.routes_page.set_add_card_code(card_code)
        self.routes_page.click_submit_card()
        self.routes_page.click_close_card_window()
        assert self.routes_page.get_payment_method_assert() == 'Tarjeta'

    def test_write_message_for_the_driver(self):
        message_for_driver = data.message_for_driver
        self.routes_page.write_driver_message_field(message_for_driver)
        assert self.routes_page.get_driver_message_field() == message_for_driver

    def test_request_blanket_and_handkerchiefs(self):
        self.routes_page.click_request_blanket_and_handkerchiefs()
        assert self.routes_page.get_assert_request_blanket_and_handkerchiefs()

    def test_request_2_ice_cream(self):
        for _ in range(2):
            self.routes_page.click_request_ice_cream()
        assert self.routes_page.get_request_ice_cream_value() == "2"

    def test_request_trip(self):
        self.routes_page.click_request_trip()
        assert self.routes_page.get_trip_confirmed().is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
