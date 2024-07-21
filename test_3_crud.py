import requests
import pytest
import allure
from used_data import UsedData


@pytest.mark.api
@pytest.mark.regression
@pytest.mark.smoke
class TestCRUD:
    @allure.feature('User Creation')
    @allure.story('Create a new user')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('This test verifies that a new user is created successfully via a POST request.')

    def test_post_create_user(self):
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
        UsedData.created_user_id = response_data['id']

        allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)




    @allure.feature('User Update')
    @allure.story('Update an existing user with PUT')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('This test verifies that an existing user is updated successfully via a PUT request.')

    def test_put_update_user(self):
        user_id = UsedData.created_user_id
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

    def test_patch_update_user(self):
        user_id = UsedData.created_user_id
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



    @allure.feature('User Deletion')
    @allure.story('Delete an existing user')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('This test verifies that an existing user is deleted successfully via a DELETE request.')

    def test_delete_user(self):
        user_id = UsedData.created_user_id

        with allure.step(f'Send DELETE request to delete user with ID {user_id}'):
            response = requests.delete(f'https://reqres.in/api/users/{user_id}')

        with allure.step('Verify that the response status code is 204'):
            assert response.status_code == 204, (
                f'There is an "Delete User" DELETE ERROR: Expected Status Code 204, but got {response.status_code}'
            )

