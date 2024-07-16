import requests
import pytest
import allure



@allure.feature('User Deletion')
@allure.story('Delete an existing user')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test verifies that an existing user is deleted successfully via a DELETE request.')
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.smoke
def test_delete_user():
    user_id = 2

    with allure.step(f'Send DELETE request to delete user with ID {user_id}'):
        response = requests.delete(f'https://reqres.in/api/users/{user_id}')

    with allure.step('Verify that the response status code is 204'):
        assert response.status_code == 204, (
            f'There is an "Delete User" DELETE ERROR: Expected Status Code 204, but got {response.status_code}'
        )

