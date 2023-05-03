from Challenging_dom.Locators.chalenging_dom_locators import MainLocators
import allure
import unittest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class MainSteps(unittest.TestCase, MainLocators):

    def __init__(self):
        super().__init__()
        self.driver = None

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")

    @allure.step
    def go_to_challenging_dom(self):
        self.driver.find_element(*MainLocators.link_text).click()

    @allure.step
    def Elements_Check(self):
        self.driver.implicitly_wait(5)
        elements_check = self.driver.find_elements(*MainLocators.elements)
        elements = []
        count = 0
        elements = elements_check[1].text.split(" ")
        for i in range(0, len(elements) - 2):
            if elements[1][-1] == "0":
                count += 1
        self.assertEqual(len(elements) - 2, count, MainLocators.success)

    def tearDown(self) -> None:
        self.driver.close()