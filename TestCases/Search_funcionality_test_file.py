import time
from Base_test_file import BaseTestClass

from Src.Pages.Page_header_file import PageHeaderNavigationBarClass


class SearchFunctionalityClass(BaseTestClass):
    def setUp(self):
        self.sleep_time = 5
        self.headerNavigationBarObj = PageHeaderNavigationBarClass(self.driver)

    def test_search_functionality(self):
        self.driver.get("https://www.amazon.com")
        self.assertIn("Amazon.com", self.driver.title)
        self.headerNavigationBarObj.fill_search_filed()
        time.sleep(self.sleep_time)  # added for visibility
        self.headerNavigationBarObj.click_on_search_submit_button()
        time.sleep(self.sleep_time)  # added for visibility

    def tearDown(self):
        self.driver.close()
