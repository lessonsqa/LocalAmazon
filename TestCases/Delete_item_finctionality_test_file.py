import time
from Base_test_file import BaseTestClass
from Src.Pages.Sign_in_page_file import SignInPageClass
from Src.Pages.Page_header_file import PageHeaderNavigationBarClass
from Src.Pages.Cart_page_file import CartPageClass


class DeleteFunctionalityClass(BaseTestClass):
    def setUp(self):
        self.sleep_time = 3
        self.signInPageObj = SignInPageClass(self.driver)
        self.headerBarObj = PageHeaderNavigationBarClass(self.driver)
        self.cartPageObj = CartPageClass(self.driver)

    def test_delete_functionality(self):
        self.signInPageObj.fast_sign_in()
        self.headerBarObj.click_on_cart_button()
        time.sleep(self.sleep_time)  # added for visibility
        self.cartPageObj.remove_all_elements_from_cart()
        time.sleep(self.sleep_time)  # added for visibility

    def tearDown(self):
        self.driver.close()
