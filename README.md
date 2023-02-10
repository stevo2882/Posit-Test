# Posit-Cloud-Test

`pip install -r requirements.txt`

Create a .env containing username and password

`EMAIL="<user_email>"`

`PASSWORD="<user_password>"`

To run tests execute the following command

`pytest tests/`

To run tests with Allure Reports

`brew install allure`

`pytest tests/ --alluredir=allure_report`

Serve the allure report locally with the following command

`allure serve allure_report`


