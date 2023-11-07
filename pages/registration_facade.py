import allure
from allure_commons.types import AttachmentType

from pages.base_facade import BaseFacade


class RegistrationFacade(BaseFacade):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.open_page()

    def open_page(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    @allure.step("Register user")
    def user_registration(self, registration_user):
        self._main_page.sing_up_button().click()
        self._registration_form_page.name_field.send_keys(registration_user.first_name)
        self._registration_form_page.last_name_field.send_keys(registration_user.last_name)
        self._registration_form_page.email_field.send_keys(registration_user.email)
        self._registration_form_page.password_field().send_keys(registration_user.password)
        self._registration_form_page.reenter_password_field().send_keys(registration_user.password)
        allure.attach(self.driver.get_screenshot_as_png(), name="screen", attachment_type=AttachmentType.PNG)
        self._registration_form_page.register_button().click()

    def check_is_user_logged_in(self):
        return len(self._garage_page.empty_garage()) > 0
