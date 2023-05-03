import unittest
from selenium.webdriver.common.by import By
from Upload_test.Locators.file_upload_locators import MainLocators
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import path

class MainSteps(unittest.TestCase, MainLocators):


    def __init__(self):
        super().__init__()
        self.driver = None

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")

    @allure.step
    def go_to_fileupload(self):
        self.driver.find_element(By.LINK_TEXT, MainLocators.link_text).click()
    @allure.step
    def file_upload(self, file_name):
        file_path = os.path.abspath(file_name)
        self.driver.find_element(By.ID, MainLocators.file_upload).send_keys(file_path)

    @allure.step
    def file_submit(self):
        self.driver.find_element(By.ID, MainLocators.file_submit).submit()

    def check_results(self):
        return self.driver.page_source.find(MainLocators.success)

    def tearDown(self) -> None:
        self.driver.close()
