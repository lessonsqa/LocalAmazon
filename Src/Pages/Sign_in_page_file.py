import time

from Src.Pages.Base_page_file import BasePageClass
from selenium.webdriver.common.by import By
from Src.Variables.Variables_file import VariablesClass


class SignInPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SignInPageLocatorsClass()

    def fill_username_field(self, username=VariablesClass.get_username()):
        userNameTextBoxElement = self.find.custom_find_element(self.locators.userNameTextFiledLocator)
        userNameTextBoxElement.send_keys(username)

    def click_on_continue_button(self):
        continueButtonElement = self.find.custom_find_element(self.locators.continueButtonLocator)
        continueButtonElement.click()

    def fill_password_field(self, password=VariablesClass.get_password()):
        userNameTextBoxElement = self.find.custom_find_element(self.locators.passwordTextFiledLocator)
        userNameTextBoxElement.send_keys(password)

    def check_the_keep_me_signed_in_checkbox(self):
        rememberMeCheckBoxElement = self.find.custom_find_element(self.locators.rememberMeCheckBoxLocator)
        rememberMeCheckBoxElement.click()

    def click_on_sign_in_button(self):
        continueButtonElement = self.find.custom_find_element(self.locators.signInButtonLocator)
        continueButtonElement.click()

    def fast_sign_in(self, username=VariablesClass.get_username(), password=VariablesClass.get_password()):
        """
        Opens Amazon.com sign in page and singes in.
        We can specify a username and password, otherwise the default values will be used.
        """
        self.driver.get(VariablesClass.amazonSignInUrl)
        # username
        self.fill_username_field(username)
        time.sleep(2)  # added to not get robot check
        self.click_on_continue_button()
        # password
        self.fill_password_field(password)
        time.sleep(2)  # added to not get robot check
        self.click_on_sign_in_button()


class SignInPageLocatorsClass:
    # Username part
    userNameTextFiledLocator = (By.ID, "ap_email")
    continueButtonLocator = (By.ID, "continue")

    # Password part
    passwordTextFiledLocator = (By.ID, "ap_password")
    rememberMeCheckBoxLocator = (By.NAME, "rememberMe")
    signInButtonLocator = (By.ID, "signInSubmit")
