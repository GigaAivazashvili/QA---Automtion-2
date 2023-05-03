from Shifting_content_Test_case.Steps.Shifting_content_steps import MainSteps
import unittest
import allure


class TestShiftingContents(unittest.TestCase):

    @allure.description("Checking on site how changes when mouse hover on button Home than going back and chacking how image changing location")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("testing some interesting things")
    @allure.suite("testing item")
    @allure.feature("check")


    def test_Home_Buttons(self):
        MainSteps.setUp(self)
        MainSteps.go_to_shifting_content(self)
        MainSteps.go_to_example_one(self)
        MainSteps.button_home_hover(self)
        MainSteps.go_back(self)
    @allure.step
    def test_pic_location(self):
        MainSteps.go_to_example_two(self)
        MainSteps.pic_loc_change(self)
        MainSteps.tearDown(self)