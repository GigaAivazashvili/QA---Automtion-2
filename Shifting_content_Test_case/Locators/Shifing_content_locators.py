from selenium.webdriver.common.by import By


class MainLocators(object):
    link_text = (By.LINK_TEXT, "Shifting Content")
    example_one = (By.LINK_TEXT, "Example 1: Menu Element")
    home_button = (By.LINK_TEXT,"Home")
    success_hover = "mouse hovered on button Home"
    example_two = (By.LINK_TEXT, "Example 2: An image")
    pic_loc = (By.TAG_NAME, "img")
    pic_loc_change = (By.XPATH, '//*[@id="content"]/div/p[3]/a')
    success_change = "picture location changed"

