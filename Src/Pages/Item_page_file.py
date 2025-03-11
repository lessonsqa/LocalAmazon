from selenium.webdriver.common.by import By
from Src.Pages.Base_page_file import BasePageClass


class ItemPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ItemPageLocatorsClass()

    def click_on_add_to_cart_button(self):
        addToCartButtonElement = self.find.custom_find_element(self.locators.addToCartButtonLocator)
        addToCartButtonElement.click()

    def add_to_cart(self):
        """add to cart if it is possible else will go to previous page"""
        try:
            self.click_on_add_to_cart_button()
            return True
        except Exception as ex:
            print("Warning : add to cart is not available. back to previous page")
            print(ex)
            self.driver.back()
            return False


class ItemPageLocatorsClass:
    addToCartButtonLocator = (By.ID, "add-to-cart-button")
