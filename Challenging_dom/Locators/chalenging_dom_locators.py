from selenium.webdriver.common.by import By


class MainLocators(object):
    link_text = By.LINK_TEXT, "Challenging DOM"
    elements = (By.TAG_NAME, "tr")
    success = "have 0 at back"