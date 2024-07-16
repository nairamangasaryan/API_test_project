import requests
import pytest
import allure


@allure.feature('User Creation')
@allure.story('Create a new user')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test verifies that a new user is created successfully via a POST request.')
@pytest.mark.api
@pytest.mark.regression
def test_post_create_user():
    user_data = {
        "name": "morpheus",
        "job": "leader"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to create a new user'):
        response = requests.post('https://reqres.in/api/users', headers=headers, json=user_data)

    with allure.step('Verify that the response status code is 201'):
        assert response.status_code == 201, (
            f'There is an "User Created" POST ERROR: Expected Status Code 201, but got {response.status_code}'
        )

    response_data = response.json()

    with allure.step('Check if the user data in the response matches the sent data'):
        assert response_data['name'] == user_data[
            'name'], 'There is an "User Created" POST ERROR: "name" field is incorrect.'
        assert response_data['job'] == user_data[
            'job'], 'There is an "User Created" POST ERROR: "job" field is incorrect.'
        assert response_data.get('id') is not None, 'There is an "User Created" POST ERROR: user "id" was not created.'
        assert response_data.get(
            'createdAt') is not None, 'There is an "User Created" POST ERROR: "createdAt" was not created.'

    allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)

