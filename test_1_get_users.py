import requests
import pytest
import allure
import time
from used_data import UsedData


@pytest.mark.api
@pytest.mark.regression
class TestGetUsers:

    @allure.feature('User List Retrieval')
    @allure.story('Get list of users from API')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('This test verifies that the API returns the list of users correctly for the specified page.')

    def test_get_list_users(self):
        page = 1
        list_data_info = UsedData.list_data_info

        with allure.step(f'Send GET request to retrieve list of users on page {page}'):
            response = requests.get(f'https://reqres.in/api/users?page={page}')

        with allure.step('Verify that the response status code is 200'):
            assert response.status_code == 200, (
                f'There is an "List of Users" GET ERROR: Expected Status Code 200, but got {response.status_code}.'
            )

        response_data = response.json()

        with allure.step('Check if the necessary information is present in the response'):
            for info in list_data_info:
                assert info in response_data, 'There is an "List of Users" GET ERROR: Needed information inconsistency.'

        if response_data['data'] is not None:
            UsedData.user_id = response_data['data'][0]['id']

        allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)


    @allure.feature('User Retrieval')
    @allure.story('Get single user from API')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        'This test verifies that the API returns the details of a single user correctly for the specified user ID.')

    def test_get_single_user(self):

        user_id = UsedData.user_id
        user_data_info = UsedData.user_data_info

        with allure.step(f'Send GET request to retrieve details of user with ID {user_id}'):
            response = requests.get(f'https://reqres.in/api/users/{user_id}')

        with allure.step('Verify that the response status code is 200'):
            assert response.status_code == 200, (
                f'There is an "Single User" GET ERROR: Expected Status Code 200, but got {response.status_code}'
            )

        response_data = response.json()

        with allure.step('Check if the necessary user information is present in the response'):
            for info in user_data_info:
                assert info in response_data['data'], f'There is an "Single User GET ERROR: {info} inconsistency.'

        with allure.step(f'Verify that the user ID in the response matches the requested user ID {user_id}'):
            assert response_data['data']['id'] == user_id, f'There is an "Single User GET ERROR: user "id" is incorrect.'

        allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)



    @allure.feature('User Retrieval')
    @allure.story('Get single user not found')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('This test verifies that the API returns a 404 status code when a user is not found.')

    def test_get_single_user_not_found(self):
        user_id = 25

        with allure.step(f'Send GET request to retrieve details of user with ID {user_id}'):
            response = requests.get(f'https://reqres.in/api/users/{user_id}')

        with allure.step('Verify that the response status code is 404'):
            assert response.status_code == 404, (
                f'There is an "Single User Not Found" GET ERROR: Expected Status Code 404, but got {response.status_code}'
            )

        with allure.step('Verify that the response JSON is empty'):
            assert response.json() == {}, 'There is an "Single User Not Found" GET ERROR: Data inconsistency'

        allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)

    @staticmethod
    @allure.feature('User Retrieval')
    @allure.story('Get delayed response')
    @allure.severity(allure.severity_level.MINOR)
    @allure.description('This test verifies that the API handles delayed responses correctly.')

    def test_delayed_response():
        list_data_info = UsedData.list_data_info

        with allure.step('Send GET request to retrieve list of users with delay'):
            start_time = time.time()
            response = requests.get(f'https://reqres.in/api/users?delay=3')
            end_time = time.time()
            elapsed_time = end_time - start_time

        with allure.step('Verify that the response status code is 200'):
            assert response.status_code == 200, (
                f'There is an "Delayed Response" GET ERROR: Expected Status Code 200, but got {response.status_code}.'
            )

        with allure.step('Verify that the response delay is approximately 3 seconds'):
            assert 2.5 < elapsed_time < 3.5, (
                f'There is an "Delayed Response" GET ERROR: Expected delay around 3 seconds, but got {elapsed_time:.2f} seconds.'
            )

        with allure.step('Verify that the response status code is 200'):
            assert response.status_code == 200, (
                f'There is an "Delayed Response" GET ERROR: Expected Status Code 200, but got {response.status_code}.'
            )

        response_data = response.json()

        with allure.step('Check if the necessary information is present in the response'):
            for info in list_data_info:
                assert info in response_data, 'There is an "Delayed Response" GET ERROR: Needed information inconsistency.'

        allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)