from selenium import webdriver
import unittest
import time

from selenium.webdriver.support.select import Select


class ck(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= "../resources/chromedriver.exe")
        print(self.driver.name)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_AllAssingnment(self):
        self.driver.get("http://cookbook.seleniumacademy.com/Config.html")
        print(self.driver.title)
        eselect_class = self.driver.find_element_by_name("make")
        eselect_selection = Select(eselect_class)
        eselect_selection.select_by_visible_text("Honda")
        eselect_selection.select_by_index(1)
        eselect_selection.select_by_value("audi")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@value='Diesel']").click()
        airbags = self.driver.find_element_by_name("airbags")

        if not airbags.is_selected():
            airbags.click()
            print(airbags.is_enabled())
            time.sleep(2)
        color = Select(self.driver.find_element_by_name("color"))
        color.select_by_value("bl")
        color.deselect_by_index(0)
        color.select_by_visible_text("Silver")
        time.sleep(2)
        




if __name__ == "__main__":
    unittest.main()

