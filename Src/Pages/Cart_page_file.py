import time

from selenium.webdriver.common.by import By
from Src.Pages.Page_header_file import PageHeaderNavigationBarClass
from Src.Pages.Base_page_file import BasePageClass


class CartPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartPageLocatorsClass()
        self.headerBarObj = PageHeaderNavigationBarClass(driver)

    def remove_first_element_from_cart(self):
        deleteElements = self.find.custom_find_elements(self.locators.deleteElementsLocator)
        firstDeleteElement = deleteElements[0]
        firstDeleteElement.click()

    def remove_all_elements_from_cart(self):
        while self.headerBarObj.get_cart_number() > 0:
            self.remove_first_element_from_cart()
            time.sleep(3)  # Fixme. why this not works without sleap. it should work since wait in custom find


class CartPageLocatorsClass:
    deleteElementsLocator = (By.CSS_SELECTOR, '[name *= "delete"]')
