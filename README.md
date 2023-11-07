# Session 27 homework
## Code from this repo required some changes to pass all the tests from the tests directory

### **Required action**
 - Check \./data/users.py file for a registration user creation
 - Run ./data/users.py as a main executable file to check it's working outside of the tests
 - Use UserCreator and RegistrationTestsDataPath variables for a conftest.py file
 - 1. The data path will be different for the test file added into the tests directory and users.py
   2. Use RegistrationTestsDataPath var to create User in conftest.py
 - Create registration_user fixture in the conftest.py file. Choose only one user with the correct password to pass a test (name=John)
 - We do add parametrization to the test!
 - Update test function with registration_user object
 - Change registration_facade class. It should work with code `registration_facade.user_registration(registration_user) `
