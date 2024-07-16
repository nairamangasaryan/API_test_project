import requests
import pytest
import allure


@allure.feature('User Registration')
@allure.story('Register a new user successfully')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test verifies that a new user is registered successfully via a POST request.')
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.smoke
def test_register_successful():
    registration_data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to register a new user'):
        response = requests.post('https://reqres.in/api/register', headers=headers, json=registration_data)

    with allure.step('Verify that the response status code is 200'):
        assert response.status_code == 200, (
            f'There is an "Successful Registration" POST ERROR: Expected Status Code 200, but got {response.status_code}'
        )

    response_data = response.json()

    with allure.step('Check if the user ID and token are present in the response'):
        assert 'id' in response_data and 'token' in response_data, 'There is an "Successful Registration" POST ERROR: "id" and "token" were not generated successfully.'

    allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)


@allure.feature('User Registration')
@allure.story('Register a new user unsuccessfully')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('This test verifies that an unsuccessful registration returns the correct error response.')
@pytest.mark.api
@pytest.mark.regression
def test_register_unsuccessful():
    registration_data = {
        "email": "eve.holt@reqres.in"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to register a new user'):
        response = requests.post('https://reqres.in/api/register', headers=headers, json=registration_data)

    with allure.step('Verify that the response status code is 400'):
        assert response.status_code == 400, (
            f'There is an "Unsuccessful Registration" POST ERROR: Expected Status Code 400, but got {response.status_code}'
        )

    response_data = response.json()

    allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)


@allure.feature('User Login')
@allure.story('Login successfully')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test verifies that a user can log in successfully via a POST request.')
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.smoke
def test_login_successful():
    login_data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to log in a user'):
        response = requests.post('https://reqres.in/api/login', headers=headers, json=login_data)

    with allure.step('Verify that the response status code is 200'):
        assert response.status_code == 200, (
            f'There is an "LOGIN - SUCCESSFUL" POST ERROR: Expected Status Code 200, but got {response.status_code}'
        )

    response_data = response.json()

    with allure.step('Check if the token is present in the response'):
        assert 'token' in response_data, 'There is an "LOGIN - SUCCESSFUL" POST ERROR: token was not generated'

    allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)


@allure.feature('User Login')
@allure.story('Login unsuccessfully')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('This test verifies that an unsuccessful login returns the correct error response.')
@pytest.mark.api
@pytest.mark.regression
def test_login_unsuccessful():
    login_data = {
        "email": "eve.holt@reqres.in"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to log in a user'):
        response = requests.post('https://reqres.in/api/login', headers=headers, json=login_data)

    with allure.step('Verify that the response status code is 400'):
        assert response.status_code == 400, (
            f'There is an "LOGIN - UNSUCCESSFUL" POST ERROR: Expected Status Code 400, but got {response.status_code}'
        )

    response_data = response.json()

    with allure.step('Check if the error message is present in the response'):
        assert 'error' in response_data, 'There is an "LOGIN - UNSUCCESSFUL" POST ERROR: error message was not generated'

    allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)

