from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver

       # checkout = self.driver.find_element(By.CSS_SELECTOR,'a[class*=btn-primary]').click()

    cards_title = (By.XPATH,'//h4[@class="card-title"]')
    card_footer = (By.XPATH,'//following::div[1]/button')
    check_out_btn = (By.CSS_SELECTOR,'a[class*=btn-primary]')


    def get_card_title(self):
        return self.driver.find_elements(*HomePage.cards_title)

    def get_card_footer(self):
        return self.driver.find_elements(*HomePage.card_footer)

    def press_on_check_out_btn(self):
        return self.driver.find_element(*HomePage.check_out_btn)
