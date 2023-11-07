import logging
import os

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import data.users
from pages.registration_facade import RegistrationFacade


"""
1. Use UserCreator and RegistrationTestsDataPath variables for a conftest.py file
 - The data path will be different for the test file added into the tests directory and users.py
 - Use RegistrationTestsDataPath var to create User in conftest.py
2. Create registration_user fixture in the conftest.py file. Choose only one user with the correct password to pass a test (name=John)
"""


@pytest.fixture
def registration_user():
    users_to_login = data.users.UserCreator.registration_users(data_path=data.users.RegistrationTestsDataPath)
    for user_to_login in users_to_login:
        if user_to_login.first_name == "John":
            yield user_to_login


# def user_data():
#     """ This function should be replaced with a new fixture registration_user
#     fixture should return only one correct user!!!"""
#     user_email = "sytischenko@gmail.com"
#     user_password = "N9Xb46SCbgd8wy!"
#     user_to_login = {
#         "email": user_email,
#         "password": user_password,
#         "remember": False
#     }
#     return user_to_login


@pytest.fixture
def logger():
    yield logging.getLogger()


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless") # Ubuntu server required option
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.close()


@pytest.fixture
def registration_facade(driver):
    facade = RegistrationFacade(driver)
    yield facade


@pytest.fixture
def session():
    session = requests.Session()
    user = yield session
    session.post(url="https://qauto2.forstudy.space/api/auth/signin", json={
        "email": "aaa@aaa.con",
        "password": "Pass 1space",
        "remember": False
    })
    session.delete(url="https://qauto2.forstudy.space/api/users")


if __name__ == "__main__":
    print(registration_user())
