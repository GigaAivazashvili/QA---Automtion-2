import unittest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class some(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://the-internet.herokuapp.com/")

    def test_check_box(self):
        self.driver.find_element(By.LINK_TEXT, "Dynamic Content").click()
        first_content = self.driver.find_element(By.CLASS_NAME, "large-10").text
        self.driver.refresh()
        second_content = self.driver.find_element(By.CLASS_NAME, "large-10").text
        assert first_content is second_content

    def tearDown(self) -> None:
        self.driver.close()