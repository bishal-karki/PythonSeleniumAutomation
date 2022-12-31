import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.ShoppingPage import ShoppingPage

from utilities.read_from_env_var import ReadFromEnvironmentVariable
import unittest


@pytest.mark.usefixtures("setup")
class TestDarazAddToCart(unittest.TestCase):

    # *************Daraz login*************
    @pytest.mark.order(1)
    def test_login(self):
        actual_title = self.driver.title
        expected_title = "Online Shopping in Nepal | Best Deals, Prices & Discounts - Daraz.com.np"
        self.assertEqual(actual_title, expected_title, "Page title does not match")

        #******************** Getting phone number and password from excel sheet*********************
        # data1 = ReadExcel()
        # ExcelPhoneNumber = data1.read_excel_phone()
        # ExcelPassword = data1.read_excel_password()

        # **********************Getting phone number and password from environment variable sheet***************
        data2 = ReadFromEnvironmentVariable()
        Environment_PhoneNumber = data2.read_env_var_phone()
        Environment_Password = data2.read_env_var_password()

        hp = HomePage(self.driver, self.wait)
        hp.login_link()
        print("Login page")
        lp = LoginPage(self.driver, self.wait)
        # *******from excel sheet***********
        # lp.textbox_phone(ExcelPhoneNumber)
        # lp.textbox_password(ExcelPassword)

        # *************from environment variable************
        lp.textbox_phone(Environment_PhoneNumber)
        lp.textbox_password(Environment_Password)

        lp.login_button()
        print("Logged in sucessfully")

    # *******************Add first item to code********************
    def test_add_to_cart_item1(self):
        item1 = ShoppingPage(self.driver, self.wait)
        item1.goto_belt()

        actual_title = self.driver.title
        expected_title = "Women's Belts In Nepal At Best Prices - Daraz.com.np"
        self.assertEqual(actual_title, expected_title, "Page title doesnot match")

        item1.select_item1()
        item1.add_to_cart()
        item1.close_add_to_cart()
        print("First item added to cart succesfully!!")
        item1.Redirect_homepage()

    # *******************Add second item to cart********************

    def test_add_to_cart_item2(self):
        item2 = ShoppingPage(self.driver, self.wait)
        item2.goto_scarves()
        actual_title = self.driver.title
        expected_title = "Pashmina Shawl Price in Nepal - Buy Scarves for Women Online - Daraz.com.np"
        self.assertEqual(actual_title, expected_title, "Page title does not match")

        # self.assertEqual(item2.actual_heading_scarves(), "Womens Shawls In Nepal", "Scarves heading Matched!")

        item2.select_item2()
        item2.add_to_cart()
        print("Second item added to cart succesfully!!")
        item2.close_add_to_cart()
        item2.Redirect_homepage()

    # *******************Add third item to cart********************
    def test_add_to_cart_item3(self):
        item3 = ShoppingPage(self.driver, self.wait)
        item3.goto_gloves()
        actual_title = self.driver.title
        expected_title = "Women's Gloves - Buy Women's Gloves at Best Price in Nepal | www.daraz.com.np"
        self.assertEqual(actual_title, expected_title, "Page title does not match")
        # self.assertEqual(item3.actual_heading_gloves(), "Women's Gloves", "Gloves heading Matched!")
        item3.select_item3()
        item3.add_to_cart()
        print("Third item added to cart succesfully!!")
        item3.close_add_to_cart()
        item3.Redirect_homepage()

    # *******************Add fourth item to cart********************
    def test_add_to_cart_item4(self):
        item4 = ShoppingPage(self.driver, self.wait)
        item4.goto_hats()
        actual_title = self.driver.title
        expected_title = "Women's Hats, Caps & Gloves In Nepal At Best Prices - Daraz.com.np"
        self.assertEqual(actual_title, expected_title, "Page title does not match")
        # self.assertEqual(item4.actual_heading_hats(), "Women's Hats & Caps", "hats heading Matched!")
        item4.select_item4()
        item4.add_to_cart()
        print("Fourth item added to cart successfully!!")
        item4.close_add_to_cart()
        item4.Redirect_homepage()

    # *******************Add fifth item to cart********************
    def test_add_to_cart_item5(self):
        item5 = ShoppingPage(self.driver, self.wait)
        item5.goto_hairs_accessories()
        actual_title = self.driver.title
        expected_title = "Women's Hair Accessories In Nepal At Best Prices - Daraz.com.np"
        self.assertEqual(actual_title, expected_title, "Page title does not match")

        item5.select_item5()
        item5.add_to_cart()
        item5.goto_cart()
        print("Fifth item added to cart successfully!!")
        print("Items i cart:")
        item5.print_items_in_cart()
        self.assertEqual(item5.num_of_items_in_cart(), 5)
        print("All items of cart are selected!!")
        item5.select_all_items_cart()
        item5.delete_items_from_cart()
        print("Items of cart are deleted!!")
