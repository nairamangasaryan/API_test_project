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
