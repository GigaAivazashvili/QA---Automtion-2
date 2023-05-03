from Shifting_content_Test_case.Locators.Shifing_content_locators import MainLocators
import allure
import unittest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color
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
    def go_to_shifting_content(self):
        self.driver.find_element(*MainLocators.link_text).click()

    @allure.step
    def go_to_example_one(self):
        self.driver.find_element(*MainLocators.example_one).click()
    @allure.step
    def button_home_hover(self):
        action = ActionChains(self.driver)
        color_not_hovered = Color.from_string(self.driver.find_element(*MainLocators.home_button).value_of_css_property('background-color'))
        self.driver.implicitly_wait(5)
        action.move_to_element(self.driver.find_element(*MainLocators.home_button)).perform()
        color_hovered = Color.from_string(self.driver.find_element(*MainLocators.home_button).value_of_css_property('background-color'))
        self.assertNotEqual(color_not_hovered, color_hovered, MainLocators.success_hover)
        self.driver.implicitly_wait(5)
    @allure.step
    def go_back(self):
        self.driver.back()

    @allure.step
    def go_to_example_two(self):
        self.driver.find_element(*MainLocators.example_two).click()
        self.driver.implicitly_wait(5)

    @allure.step
    def pic_loc_change(self):
        main_data = self.driver.find_element(MainLocators.pic_loc)
        self.driver.find_element(MainLocators.pic_loc_change).click()
        secondary_data = self.driver.find_element(MainLocators.pic_loc)
        self.assertNotEqual(main_data, secondary_data, MainLocators.success_change)

    def tearDown(self) -> None:
        self.driver.close()