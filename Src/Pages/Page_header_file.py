from selenium.webdriver.common.by import By
from Src.Pages.Base_page_file import BasePageClass
from Src.Variables.Variables_file import VariablesClass


class PageHeaderNavigationBarClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PageHeaderNavigationBarLocatorsClass()

    def fill_search_filed(self, search_text=VariablesClass.defSearchText):
        searchTextBoxElement = self.find.custom_find_element(self.locators.searchTextBoxLocator)
        searchTextBoxElement.clear()
        searchTextBoxElement.send_keys(search_text)

    def click_on_search_submit_button(self):
        searchSubmitButtonElement = self.find.custom_find_element(self.locators.searchSubmitButtonLocator)
        searchSubmitButtonElement.click()

    def click_on_cart_button(self):
        cartButtonElement = self.find.custom_find_element(self.locators.cartButtonLocator)
        cartButtonElement.click()

    def get_cart_number(self):
        cartButtonElement = self.find.custom_find_element(self.locators.cartButtonLocator)
        return int(cartButtonElement.text)


class PageHeaderNavigationBarLocatorsClass:
    searchTextBoxLocator = (By.ID, "twotabsearchtextbox")
    searchSubmitButtonLocator = (By.ID, "nav-search-submit-button")
    cartButtonLocator = (By.ID, "nav-cart-count")
