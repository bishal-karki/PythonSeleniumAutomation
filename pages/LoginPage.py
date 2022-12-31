import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def textbox_phone(self,phone):
        phone_number = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="text" i]')))
        phone_number.send_keys(phone)

    def textbox_password(self,pass_word):
        password = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="password" i]')))
        password.send_keys(pass_word)

    def login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[2]/form/div/div[2]/div[1]/button')))
        login_button.click()
        time.sleep(5)
