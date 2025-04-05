from Src.Pages.Base_page_file import BasePageClass
from selenium.webdriver.common.by import By


class SearchResultsPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SearchResultsLocatorsClass()

    def click_on_nth_item(self, n: int = 1):
        foundElements = self.find.custom_find_elements(self.locators.foundItemsLocator)
        foundItemElement = foundElements[n//2 + n]
        foundItemElement.click()

    def get_nth_item(self, n: int = 1):
        foundElements = self.find.custom_find_elements(self.locators.foundItemsLocator)
        return foundElements[n//2 + n]

    def get_nth_item_price(self, n: int = 1):
        foundElements = self.find.custom_find_elements(self.locators.foundItemsPriceLocator)
        return foundElements[n//2 + n]


class SearchResultsLocatorsClass:
    foundItemsLocator = (By.CSS_SELECTOR,
                         ".a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
    # foundItemsPriceLocator = (By.XPATH, "//span[@class='a-price']")
    foundItemsPriceLocator = (By.CLASS_NAME, "a-price")
