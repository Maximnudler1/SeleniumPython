import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging

import PageObject
from utilites.BaseClass import Baseclass
from PageObject.RegisterPage import RegisterPage
from PageObject.homePage import HomePage
from PageObject.checkOutPage import CheckOutPage


class TestOne(Baseclass):
    def test_india(self):
        log = self.getLogger()

        reg_p = RegisterPage(self.driver)
        reg_p.go_to_shop_page().click()

        homePage = HomePage(self.driver)
        cards = homePage.get_card_title()
        log.info("card title is :")
        i = 0
        for card in cards:
            i += 1
            if card.text == "Blackberry":
               homePage.get_card_footer()[i].click()

        homePage.press_on_check_out_btn().click()

        check_out = CheckOutPage(self.driver)
        check_out_price = int(check_out.get_total_price().text[3:])

        check_out.get_proceed_to_final_check_out_btn().click()
        check_out.insert_a_country_to_ship().send_keys('India')
        self.verify_link_presence('India')
        self.driver.find_element(By.LINK_TEXT,'India').click()
        input_value = check_out.insert_a_country_to_ship().get_attribute('value')
        print(input_value)
        check_out.mark_check_box().click()
        check_out.submit_button().click()
        assert 'Thank you!' in check_out.print_success_message().text


    def test_register(self):

        log = self.getLogger()

        reg_p = RegisterPage(self.driver)
        self.driver.get('https://rahulshettyacademy.com/angularpractice')
        self.driver.refresh()
        reg_p.insert_name().send_keys('maxim')
        reg_p.insert_email().send_keys("maxim@gmail.com")
        reg_p.insert_password().send_keys('maxim100')
        reg_p.insert_birthday().send_keys('28101994')
        reg_p.select_student_status()
        reg_p.select_male()
        reg_p.select_ice_cream()
        reg_p.press_submit_btn()
        assert "The Form has been submitted successfully!" in reg_p.alert_message_pop_up().text
        log.info("finish second test")


        # checkout = self.driver.find_element(By.CSS_SELECTOR,'a[class*=btn-primary]').click()
        # total_price = int(self.driver.find_element(By.XPATH,'//tbody/tr[1]/td[3]').text[3:])

        # self.driver.find_element(By.CSS_SELECTOR,'button[class*=btn-success]').click()
        # self.driver.find_element(By.CSS_SELECTOR,'#country').send_keys("india")
        # wait = WebDriverWait(self.driver,10)
        # wait.until(EC.presence_of_element_located((By.LINK_TEXT,'India')))
        # self.driver.find_element(By.LINK_TEXT,'India').click()
        # input_value = self.driver.find_element(By.CSS_SELECTOR,'#country').get_attribute('value')
        # print(input_value)
        # time.sleep(5)
        # self.driver.find_element(By.CSS_SELECTOR,"label[for='checkbox2']").click()
        # self.driver.find_element(By.XPATH,'//input[@type="submit"]').click()
        # success = self.driver.find_element(By.CSS_SELECTOR,'div[class*= alert]').text
        # print(success)

    #
    # def test_price_diffrence(self):
    #
    #
    #     item_page1 = []
    #     item_page2 = []
    #     # driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
    #
    #     self.driver.find_element(By.CSS_SELECTOR,'.search-keyword').send_keys('ber')
    #     time.sleep(1)
    #     products = self.driver.find_elements(By.XPATH,'//div[@class="products"]/div')
    #     print(len(products))
    #
    #
    #     add_to_cart_products = self.driver.find_elements(By.XPATH,'//button[text()="ADD TO CART"]')
    #
    #     for item in add_to_cart_products:
    #         item_page1.append(item.find_element(By.XPATH,'parent::div/parent::div/h4').text)
    #         item.click()
    #
    #     print(item_page1)
    #     basket = self.driver.find_element(By.XPATH,'//img[@alt="Cart"]').click()
    #     proceed_to_checkout = self.driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']").click()
    #
    #     wait = WebDriverWait(self.driver,7)
    #     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.promoCode')))
    #
    #     vegteb = self.driver.find_elements(By.CSS_SELECTOR,'.product-name')
    #     for v in vegteb:
    #         item_page2.append(v.text)
    #
    #     assert  item_page1 == item_page2
    #     print(item_page2)
    #
    #     sum = 0
    #     amounts = self.driver.find_elements(By.XPATH,'//tr/td[5]/p')
    #     for amount in amounts:
    #         sum += int(amount.text)
    #
    #
    #
    #     total_amount = self.driver.find_element(By.CSS_SELECTOR,'.totAmt').text
    #     total_amount = int(total_amount)
    #
    #     assert sum == total_amount