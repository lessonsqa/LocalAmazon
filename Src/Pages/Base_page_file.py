from Common.Find.Custom_find_file import CustomFindClass


class BasePageClass:
    def __init__(self, driver):
        self.driver = driver
        self.find = CustomFindClass(driver)
