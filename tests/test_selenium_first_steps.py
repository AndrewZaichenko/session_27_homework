import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@allure.feature("Beautiful tests")
@allure.issue(url="https://google.com", name="Link for very important bag")
@allure.link(url="https://google.com", name="Link to TestRail")
def test_registration(logger, registration_facade, session, registration_user):
    """ This test should be fixed to use registration_user instead of john_user fixture"""
    logger.info("User register test")
    # Replace  registration_facade.registration_user to registration_facade.user_registration(registration_user)
    # registration_facade.registration_user("test",
    #                                       'testlastname',
    #                                       "sytischenko@gmail.com",
    #                                       "N9Xb46SCbgd8wy!",
    #                                       "N9Xb46SCbgd8wy!")
    # assert registration_facade.check_is_user_logged_in()
    registration_facade.user_registration(registration_user)
    assert registration_facade.check_is_user_logged_in()


def test_failed_registration_test(logger, driver):
    driver.get("https://qauto2.forstudy.space/panel/settings")
    try:
        delete_users = driver.find_element(By.XPATH, "//button[text()='Remove my account']")
    except NoSuchElementException:
        logger.critical("No element found")
        # raise RuntimeError("No element found //button[text()='Remove my account']")  # will fail this test
    else:
        delete_users.click()
        delete_users_confirm = driver.find_element(By.XPATH, "//button[text()='Remove']")
        delete_users_confirm.click()
