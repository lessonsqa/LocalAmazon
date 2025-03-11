import time

from Base_test_file import BaseTestClass

from Src.Pages.Sign_in_page_file import SignInPageClass
from Src.Pages.Page_header_file import PageHeaderNavigationBarClass
from Src.Pages.Search_results_page_file import SearchResultsPageClass
from Src.Pages.Item_page_file import ItemPageClass
from Src.Pages.Cart_page_file import CartPageClass


class AmazonActionClass(BaseTestClass):
    def setUp(self):
        self.sleep_time = 3  # set to 0 for fast run
        self.signInPageObj = SignInPageClass(self.driver)
        self.homePageObj = PageHeaderNavigationBarClass(self.driver)
        self.resultPageObj = SearchResultsPageClass(self.driver)
        self.itemPageObj = ItemPageClass(self.driver)
        self.cartPageObj = CartPageClass(self.driver)

    def test_amazon_sign_in_and_add_element(self):
        """Log in, search an item, add to cart"""
        # go to amazon and sign in
        self.signInPageObj.fast_sign_in()
        # search
        self.homePageObj.fill_search_filed()
        time.sleep(self.sleep_time)  # added for visibility
        self.homePageObj.click_on_search_submit_button()
        time.sleep(self.sleep_time)  # added for visibility
        # select an item
        for i in range(1, 10):
            self.resultPageObj.click_on_nth_item(i)
            time.sleep(self.sleep_time)  # added for visibility
        # add to cart
            status = self.itemPageObj.add_to_cart()
            if status:
                break

        time.sleep(self.sleep_time)  # added for visibility

    def tearDown(self):
        self.driver.close()
