
import requests
import pytest
import allure


@allure.feature('User Update')
@allure.story('Update an existing user with PUT')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test verifies that an existing user is updated successfully via a PUT request.')
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.smoke
def test_put_update_user():
    user_id = 2
    user_data_update = {
        "name": "morpheus",
        "job": "zion resident"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step(f'Send PUT request to update user with ID {user_id}'):
        response = requests.put(f'https://reqres.in/api/users/{user_id}', headers=headers, json=user_data_update)

    with allure.step('Verify that the response status code is 200'):
        assert response.status_code == 200, (
            f'There is an "User Update" PUT ERROR: Expected Status Code 200, but got {response.status_code}'
        )

    response_data = response.json()

    with allure.step('Check if the user data in the response matches the updated data'):
        assert response_data['name'] == user_data_update[
            'name'], 'There is an "User Update" PUT ERROR: "name" field is incorrect.'
        assert response_data['job'] == user_data_update[
            'job'], 'There is an "User Update" PUT ERROR: "job" field is incorrect.'

    allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)


@allure.feature('User Update')
@allure.story('Update an existing user with PATCH')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test verifies that an existing user is updated successfully via a PATCH request.')
@pytest.mark.api
@pytest.mark.regression
def test_patch_update_user():
    user_id = 2
    user_data_update = {
        "name": "morpheus",
        "job": "zion resident"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step(f'Send PATCH request to update user with ID {user_id}'):
        response = requests.patch(f'https://reqres.in/api/users/{user_id}', headers=headers, json=user_data_update)

    with allure.step('Verify that the response status code is 200'):
        assert response.status_code == 200, (
            f'There is an "User Update" PATCH ERROR: Expected Status Code 200, but got {response.status_code}'
        )

    response_data = response.json()

    with allure.step('Check if the user data in the response matches the updated data'):
        assert response_data['name'] == user_data_update[
            'name'], 'There is an "User Update" PATCH ERROR: "name" field is incorrect.'
        assert response_data['job'] == user_data_update[
            'job'], 'There is an "User Update" PATCH ERROR: "job" field is incorrect.'

    allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)

