import requests
import pytest
import allure


@allure.feature('User List Retrieval')
@allure.story('Get list of users from API')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test verifies that the API returns the list of users correctly for the specified page.')
@pytest.mark.api
@pytest.mark.regression
def test_get_list_users():
    page = 5
    list_data_info = ['page', 'per_page', 'total', 'total_pages', 'data']

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

    allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)



@allure.feature('User Retrieval')
@allure.story('Get single user from API')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(
    'This test verifies that the API returns the details of a single user correctly for the specified user ID.')
@pytest.mark.api
@pytest.mark.regression
def test_get_single_user():
    user_id = 2
    user_data_info = ['id', 'email', 'first_name', 'last_name', 'avatar']

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
@pytest.mark.api
@pytest.mark.regression
def test_get_single_user_not_found():
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


@allure.feature('Resource Retrieval')
@allure.story('Get list of resources')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test verifies that the API returns the list of resources correctly.')
@pytest.mark.api
@pytest.mark.regression
def test_get_list_resources():
    resource_data_info = ['page', 'per_page', 'total', 'total_pages', 'data']

    with allure.step('Send GET request to retrieve list of resources'):
        response = requests.get('https://reqres.in/api/unknown')

    with allure.step('Verify that the response status code is 200'):
        assert response.status_code == 200, (
            f'There is an "List of Resources" GET ERROR: Expected Status Code 200, but got {response.status_code}'
        )

    response_data = response.json()

    with allure.step('Check if the necessary information is present in the response'):
        for info in resource_data_info:
            assert info in response_data, f'There is an "List of Resources" GET ERROR: {info} inconsistency.'

    allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)


@allure.feature('Resource Retrieval')
@allure.story('Get single resource')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(
    'This test verifies that the API returns the details of a single resource correctly for the specified resource ID.')
@pytest.mark.api
@pytest.mark.regression
def test_get_single_resource():
    resource_dat_info = ['id', 'name', 'year', 'color', 'pantone_value']
    resource_id = 3

    with allure.step(f'Send GET request to retrieve details of resource with ID {resource_id}'):
        response = requests.get(f'https://reqres.in/api/unknown/{resource_id}')

    with allure.step('Verify that the response status code is 200'):
        assert response.status_code == 200, (
            f'There is an "Single Resource" GET ERROR: Expected Status Code 200, but got {response.status_code}'
        )

    response_data = response.json()

    with allure.step('Check if the necessary resource information is present in the response'):
        for info in resource_dat_info:
            assert info in response_data['data'], 'There is an "Single Resource" GET ERROR: Data inconsistency'

    allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)


@allure.feature('Resource Retrieval')
@allure.story('Get single resource not found')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('This test verifies that the API returns a 404 status code when a resource is not found.')
@pytest.mark.api
@pytest.mark.regression
def test_get_single_resource_not_found():
    resource_id = 25

    with allure.step(f'Send GET request to retrieve details of resource with ID {resource_id}'):
        response = requests.get(f'https://reqres.in/api/unknown/{resource_id}')

    with allure.step('Verify that the response status code is 404'):
        assert response.status_code == 404, (
            f'There is an "Single Resource Not Found" GET ERROR: Expected Status Code 404, but got {response.status_code}'
        )

    with allure.step('Verify that the response JSON is empty'):
        assert response.json() == {}, 'There is an "Single Resource Not Found" GET ERROR: Data inconsistency'

    allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)




@allure.feature('User Retrieval')
@allure.story('Get delayed response')
@allure.severity(allure.severity_level.MINOR)
@allure.description('This test verifies that the API handles delayed responses correctly.')
@pytest.mark.api
@pytest.mark.regression
def test_delayed_response():
    list_data_info = ['page', 'per_page', 'total', 'total_pages', 'data']

    with allure.step('Send GET request to retrieve list of users with delay'):
        response = requests.get(f'https://reqres.in/api/users?delay=3')

    with allure.step('Verify that the response status code is 200'):
        assert response.status_code == 200, (
            f'There is an "Delayed Response" GET ERROR: Expected Status Code 200, but got {response.status_code}.'
        )

    response_data = response.json()

    with allure.step('Check if the necessary information is present in the response'):
        for info in list_data_info:
            assert info in response_data, 'There is an "Delayed Response" GET ERROR: Needed information inconsistency.'

    allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)
