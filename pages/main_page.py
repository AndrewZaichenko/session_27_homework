from pages import By

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.sing_up_button = lambda: self.driver.find_element(By.XPATH, "//button[text()='Sign up']")