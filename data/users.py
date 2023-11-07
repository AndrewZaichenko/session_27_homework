import json
import logging
import os

logger = logging.getLogger()

RegistrationTestsDataPath = "../data"  # Should be in a separate module or in __init__.py

# Different User models could be created for the different test modules
# Password has to be from 8 to 15 characters long and contain at least one integer, one capital, and one small letter
REGISTRATION_USER_MODEL = {
    "first_name": "user first name",
    "last_name": "user last name",
    "email": 'user_email',
    "password": 'user_password',
    "remember": bool
}


class UserConfigReader:
    """ Class to read all user-required data from all possible config files
    JSON files reading usage for the homework completion will be enough """
    DEFAULT_PATH = "sample_users_with_id.json"

    # Used for not to read file for everytime for fixtures with a function scope
    @classmethod
    def read_json_config(cls, path: str = "", user_model: dict = None):
        path = cls.DEFAULT_PATH if not path else path
        with open(path) as json_config_file:
            # Get all data from the config file
            config_json = json.load(json_config_file)
        if user_model:
            user_config_json = []
            for index, json_object in enumerate(config_json):
                """Replace json array objects index with filtered json objects(python dictionaries)"""
                user_config_json.append(cls.json_filter(user_model, json_object))
            config_json = user_config_json
        return config_json

    @classmethod
    def json_filter(cls, user_model, json_object: dict):
        """ Filter required fields to filtered_dict var"""
        filtered_object = {}
        for key in user_model:
            filtered_object[key] = json_object.get(key)
        logger.info(f"User model found: {filtered_object}")
        return filtered_object


class UserCreator:
    def __init__(self, **user_config):
        """ Create User attributes from incoming JSON object (Associative array)"""
        self.__dict__.update(user_config)

    @classmethod
    def registration_users(cls, data_path='.'):
        """Method to create registration user only.
        Additional methods could be created for happy path and sad path testing cases"""
        path = os.path.join(data_path, "sample_users_with_id.json")
        model = REGISTRATION_USER_MODEL
        config_json = UserConfigReader.read_json_config(path, model)
        return [cls(**user_config) for user_config in config_json]


if __name__ == "__main__":
    registration_user_config = UserConfigReader.read_json_config(user_model=REGISTRATION_USER_MODEL)
    print(registration_user_config)
    registration_users = UserCreator.registration_users()
    print(registration_users)
    # Need to create registration_user fixture in the conftest.py for modified registration test
