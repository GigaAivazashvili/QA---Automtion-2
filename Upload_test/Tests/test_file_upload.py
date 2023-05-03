import allure
from Upload_test.Steps.file_upload_steps import MainSteps
import unittest

class TestFileUpload(unittest.TestCase):

    @allure.description("Checking Test case for uploading 'pythonProject' file on site")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Upload 'pythonProject' file")
    @allure.suite("File Upload Test case")
    @allure.feature("Upload")

    def test_file_upload(self):
        MainSteps.setUp(self)
        MainSteps.go_to_fileupload(self)
        MainSteps.file_upload(self, "C:\\Users\\User\\PycharmProjects\\pythonProject")
        MainSteps.file_submit(self)
        self.assertTrue(MainSteps.check_results(self))
        MainSteps.tearDown(self)
