from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver


    total_price = (By.XPATH,'//tbody/tr[1]/td[3]')
    proceed_to_final_check_out = (By.CSS_SELECTOR,'button[class*=btn-success]')
    ship_to_country = (By.CSS_SELECTOR,'#country')
    check_box = (By.CSS_SELECTOR,"label[for='checkbox2']")
    submit_btn = (By.XPATH,'//input[@type="submit"]')
    success_message = (By.CSS_SELECTOR,'div[class*= alert]')


    def get_total_price(self):
        return self.driver.find_element(*CheckOutPage.total_price)

    def get_proceed_to_final_check_out_btn(self):
        return self.driver.find_element(*CheckOutPage.proceed_to_final_check_out)

    def insert_a_country_to_ship(self):
        return self.driver.find_element(*CheckOutPage.ship_to_country)

    def mark_check_box(self):
        return self.driver.find_element(*CheckOutPage.check_box)

    def submit_button(self):
        return self.driver.find_element(*CheckOutPage.submit_btn)

    def print_success_message(self):
        return self.driver.find_element(*CheckOutPage.success_message)