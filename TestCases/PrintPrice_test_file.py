import time
from Base_test_file import BaseTestClass
from Src.Pages.Sign_in_page_file import SignInPageClass
from Src.Pages.Page_header_file import PageHeaderNavigationBarClass
from Src.Pages.Search_results_page_file import SearchResultsPageClass


class PriceCheckClass(BaseTestClass):
    def setUp(self):
        self.sleep_time = 5
        self.signInPageObj = SignInPageClass(self.driver)
        self.headerNavigationBarObj = PageHeaderNavigationBarClass(self.driver)
        self.resultPageObj = SearchResultsPageClass(self.driver)

    def test_price(self):
        self.signInPageObj.fast_sign_in()
        self.headerNavigationBarObj.fill_search_filed("agv helmet")
        time.sleep(self.sleep_time)  # added for visibility
        self.headerNavigationBarObj.click_on_search_submit_button()
        time.sleep(self.sleep_time)  # added for visibility
        firstItem = self.resultPageObj.get_nth_item_price(0)
        print(firstItem.text)
        self.resultPageObj.click_on_nth_item(0)

    def tearDown(self):
        self.driver.close()
