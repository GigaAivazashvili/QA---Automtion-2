import allure
from Shifting_content_Test_case.Steps.Shifting_content_steps import MainSteps
import unittest

class Shiftingcontent(unittest.TestCase):

    @allure.description("Checking Test case for uploading 'pythonProject' file on site")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Upload 'pythonProject' file")
    @allure.suite("File Upload Test case")
    @allure.feature("Upload")
    @allure.step
    def Test_Home_Button(self):
        MainSteps.setUp(self)
        MainSteps.go_to_shiftingcontent(self)
        MainSteps.go_to_exampleone(self)
        MainSteps.button_home_hover(self)
        MainSteps.go_back(self)
    # @allure.step
    # def Test_pic_location(self):
        MainSteps.go_to_exampletwo(self)
        MainSteps.pic_loc_change(self)
        MainSteps.tearDown(self)