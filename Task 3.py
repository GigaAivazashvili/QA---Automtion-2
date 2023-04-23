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
        self.driver.find_element(By.LINK_TEXT, "File Download").click()
        self.driver.find_element(By.LINK_TEXT, "test.txt").click()

    def tearDown(self) -> None:
        self.driver.close()