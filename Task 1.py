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
        self.driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()

        self.driver.find_element(By.TAG_NAME, "button").click()
        self.driver.find_element(By.TAG_NAME, "button").click()
        self.driver.find_element(By.TAG_NAME, "button").click()
        self.driver.find_element(By.TAG_NAME, "button").click()
        self.driver.find_element(By.TAG_NAME, "button").click()
        self.driver.find_element(By.TAG_NAME, "button").click()
        self.driver.find_element(By.TAG_NAME, "button").click()
        self.driver.find_element(By.TAG_NAME, "button").click()
        self.driver.find_element(By.TAG_NAME, "button").click()
        self.driver.find_element(By.TAG_NAME, "button").click()

        self.driver.find_element(By.CLASS_NAME,"added-manually").click()
        self.driver.find_element(By.CLASS_NAME,"added-manually").click()
        self.driver.find_element(By.CLASS_NAME,"added-manually").click()
        self.driver.find_element(By.CLASS_NAME,"added-manually").click()
        self.driver.find_element(By.CLASS_NAME,"added-manually").click()
        self.driver.find_element(By.CLASS_NAME,"added-manually").click()
        self.driver.find_element(By.CLASS_NAME,"added-manually").click()

        elements_amount = self.driver.find_elements(By.CLASS_NAME, "added-manually")
        assert 3 == len(elements_amount)

    def tearDown(self) -> None:
        self.driver.close()