import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class ShoppingPage:
    hover_womens_fashion_xpath = '//*[@id="Level_1_Category_No8"]'
    hover_accessories_xpath = '//*[@id="J_8018372580"]/div/ul/ul[1]/li[5]'
    hover_belt_xpath = '//*[@id="J_8018372580"]/div/ul/ul[1]/li[5]/ul/li[1]'
    hover_scarves_xpath = '//*[@id="J_8018372580"]/div/ul/ul[1]/li[5]/ul/li[2]'
    hover_gloves_xpath = '//*[@id="J_8018372580"]/div/ul/ul[1]/li[5]/ul/li[3]'
    hover_hats_xpath = '//*[@id="J_8018372580"]/div/ul/ul[1]/li[5]/ul/li[4]'
    hover_hairs_accessories_xpath = '//*[@id="J_8018372580"]/div/ul/ul[1]/li[5]/ul/li[5]'
    item1_xpath = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/a'
    item2_xpath = '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div[1]'
    item3_xpath = '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[1]'
    item4_xpath = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]'
    item5_xpath = '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div[1]'
    items_in_cart = "cart-item"

    add_to_cart_xpath = '//*[@id="module_add_to_cart"]/div/button[2]'
    close_add_to_cart_xpath = '/html/body/div[8]/div/div[2]/a/i'
    homepage_xpath = '//*[@id="topActionHeader"]/div[1]/div[2]/div/div[1]/a'
    goto_cart_xpath = '//*[@id="dialog-body-1"]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/button[2]'
    select_all = '//*[@id="listHeader_H"]/div/div/div[1]/label/input'
    delete_cart_xpath = '//*[@id="listHeader_H"]/div/div/div[2]/div'
    remove_xpath = '/html/body/div[8]/div/div/div[3]/div/button[2]'

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.actions = ActionChains(self.driver)

    def goto_belt(self):
        WomensFashion = self.driver.find_element(By.XPATH, self.hover_womens_fashion_xpath)
        Accessories = self.driver.find_element(By.XPATH, self.hover_accessories_xpath)
        Belt = self.driver.find_element(By.XPATH, self.hover_belt_xpath)

        self.actions.move_to_element(WomensFashion).move_to_element(Accessories).move_to_element(Belt).click().perform()

    def goto_scarves(self):
        WomensFashion = self.driver.find_element(By.XPATH, self.hover_womens_fashion_xpath)
        Accessories = self.driver.find_element(By.XPATH, self.hover_accessories_xpath)
        scarves = self.driver.find_element(By.XPATH, self.hover_scarves_xpath)
        self.actions.move_to_element(WomensFashion).move_to_element(Accessories).move_to_element(
            scarves).click().perform()

    def goto_gloves(self):
        WomensFashion = self.driver.find_element(By.XPATH, self.hover_womens_fashion_xpath)
        Accessories = self.driver.find_element(By.XPATH, self.hover_accessories_xpath)
        gloves = self.driver.find_element(By.XPATH, self.hover_gloves_xpath)
        self.actions.move_to_element(WomensFashion).move_to_element(Accessories).move_to_element(
            gloves).click().perform()

    def goto_hats(self):
        WomensFashion = self.driver.find_element(By.XPATH, self.hover_womens_fashion_xpath)
        Accessories = self.driver.find_element(By.XPATH, self.hover_accessories_xpath)
        hats = self.driver.find_element(By.XPATH, self.hover_hats_xpath)
        self.actions.move_to_element(WomensFashion).move_to_element(Accessories).move_to_element(hats).click().perform()

    def goto_hairs_accessories(self):
        WomensFashion = self.driver.find_element(By.XPATH, self.hover_womens_fashion_xpath)
        Accessories = self.driver.find_element(By.XPATH, self.hover_accessories_xpath)
        hairs_accessories = self.driver.find_element(By.XPATH, self.hover_hairs_accessories_xpath)

        self.actions.move_to_element(WomensFashion).move_to_element(Accessories).move_to_element(
            hairs_accessories).click().perform()

    def select_item1(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.item1_xpath))).click()

    def select_item2(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.item2_xpath))).click()

    def select_item3(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.item3_xpath))).click()

    def select_item4(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.item4_xpath))).click()

    def select_item5(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.item5_xpath))).click()

    def add_to_cart(self):
        AddToCart = self.driver.find_element(By.XPATH, self.add_to_cart_xpath)
        AddToCart.click()

    def close_add_to_cart(self):
        close_cart = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.close_add_to_cart_xpath)))
        close_cart.click()

    def Redirect_homepage(self):
        HomePage = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.homepage_xpath)))
        HomePage.click()

    def goto_cart(self):
        goto_cart = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.goto_cart_xpath)))
        goto_cart.click()
        time.sleep(3)

    def print_items_in_cart(self):
        all_items_cart = self.driver.find_elements(By.CLASS_NAME, self.items_in_cart)
        i = 1
        for item in all_items_cart:
            print(f"item {i} : {item.text}\n")
            i += 1

    def num_of_items_in_cart(self):
        total_items = len(self.driver.find_elements(By.CLASS_NAME, self.items_in_cart))
        return total_items

    def select_all_items_cart(self):
        self.driver.find_element(By.XPATH, self.select_all).click()
        time.sleep(3)

    def delete_items_from_cart(self):
        self.driver.find_element(By.XPATH, self.delete_cart_xpath).click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, self.remove_xpath).click()
        time.sleep(3)
