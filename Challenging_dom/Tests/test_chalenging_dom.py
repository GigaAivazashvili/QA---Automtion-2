from Challenging_dom.Steps.chalenging_dom_steps import MainSteps
import unittest
import allure


class TestChallengingDom(unittest.TestCase):

    @allure.description("checking if on site first line elements have 0 in beck")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("testing some interesting things")
    @allure.suite("testing item")
    @allure.feature("check")
    def test_challenging_dom(self):
        MainSteps.setUp(self)
        MainSteps.go_to_challenging_dom(self)
        MainSteps.Elements_Check(self)
        MainSteps.tearDown(self)