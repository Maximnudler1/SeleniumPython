from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver


    name = (By.CSS_SELECTOR,"div[class='form-group'] input[name='name']")
    email = (By.CSS_SELECTOR,'input[name="email"]')
    password = (By.CSS_SELECTOR,'#exampleInputPassword1')
    ice_cream_radio_checkbox = (By.CSS_SELECTOR,'#exampleCheck1')
    select_gender = (By.CSS_SELECTOR,'#exampleFormControlSelect1')


    employment_status_student = (By.CSS_SELECTOR,'#inlineRadio1')
    employment_status_employed = (By.CSS_SELECTOR,'#inlineRadio2')

    birth_date = (By.CSS_SELECTOR,'input[name=bday]')
    submit_btn = (By.CSS_SELECTOR,'.btn-success')
    shop_link = (By.XPATH,"//a[@href='/angularpractice/shop']")

    alert_message = (By.CSS_SELECTOR,'.alert-success')

    def insert_name(self):
        return self.driver.find_element(*RegisterPage.name)

    def insert_email(self):
        return self.driver.find_element(*RegisterPage.email)

    def insert_password(self):
        return self.driver.find_element(*RegisterPage.password)

    def select_male(self):
        select = Select(self.driver.find_element(*RegisterPage.select_gender))
        return select.select_by_visible_text('Male')

    def select_female(self):
        select = Select(self.driver.find_element(*RegisterPage.select_gender))
        return select.select_by_visible_text('Female')

    def select_student_status(self):
        return self.driver.find_element(*RegisterPage.employment_status_student).click()

    def select_employed_status(self):
        return self.driver.find_element(*RegisterPage.employment_status_employed).click()

    def insert_birthday(self):
        return self.driver.find_element(*RegisterPage.birth_date)

    def press_submit_btn(self):
        return self.driver.find_element(*RegisterPage.submit_btn).click()

    def go_to_shop_page(self):
        return self.driver.find_element(*RegisterPage.shop_link)
    def select_ice_cream(self):
        return self.driver.find_element(*RegisterPage.ice_cream_radio_checkbox).click()

    def alert_message_pop_up(self):
        return self.driver.find_element(*RegisterPage.alert_message)

