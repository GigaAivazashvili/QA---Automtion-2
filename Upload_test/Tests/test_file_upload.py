from tests.Steps.file_upload_steps import MainSteps
import unittest
import allure

class testFileUpload(unittest.TestCase):

    def test_file_upload(self):
        MainSteps.setUp(self)
        MainSteps.go_to_fileupload(self)
        MainSteps.file_upload(self, "Steps")
        MainSteps.file_submit(self)
        self.assertTrue(MainSteps.check_results(self))
        MainSteps.tearDown(self)
