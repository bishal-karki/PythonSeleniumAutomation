import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def login_link(self):
        login = self.wait.until(EC.element_to_be_clickable((By.ID, 'anonLogin')))
        login.click()
        time.sleep(5)
