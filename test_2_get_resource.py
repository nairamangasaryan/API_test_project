import requests
import pytest
import allure
from used_data import UsedData


@pytest.mark.api
@pytest.mark.regression
class TestGetResource:
    @allure.feature('Resource Retrieval')
    @allure.story('Get list of resources')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('This test verifies that the API returns the list of resources correctly.')

    def test_get_list_resources(self):
        list_data_info = UsedData.list_data_info

        with allure.step('Send GET request to retrieve list of resources'):
            response = requests.get('https://reqres.in/api/unknown')

        with allure.step('Verify that the response status code is 200'):
            assert response.status_code == 200, (
                f'There is an "List of Resources" GET ERROR: Expected Status Code 200, but got {response.status_code}'
            )

        response_data = response.json()

        with allure.step('Check if the necessary information is present in the response'):
            for info in list_data_info:
                assert info in response_data, f'There is an "List of Resources" GET ERROR: {info} inconsistency.'

        if response_data['data'] is not None:
            UsedData.resource_id = response_data['data'][0]['id']
        allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)


    @allure.feature('Resource Retrieval')
    @allure.story('Get single resource')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        'This test verifies that the API returns the details of a single resource correctly for the specified resource ID.')

    def test_get_single_resource(self):
        resource_data_info = UsedData.resource_data_info
        resource_id = UsedData.resource_id

        with allure.step(f'Send GET request to retrieve details of resource with ID {resource_id}'):
            response = requests.get(f'https://reqres.in/api/unknown/{resource_id}')

        with allure.step('Verify that the response status code is 200'):
            assert response.status_code == 200, (
                f'There is an "Single Resource" GET ERROR: Expected Status Code 200, but got {response.status_code}'
            )

        response_data = response.json()

        with allure.step('Check if the necessary resource information is present in the response'):
            for info in resource_data_info:
                assert info in response_data['data'], 'There is an "Single Resource" GET ERROR: Data inconsistency'

        allure.attach(response.text, name='Response JSON', attachment_type=allure.attachment_type.JSON)


    @allure.feature('Resource Retrieval')
    @allure.story('Get single resource not found')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('This test verifies that the API returns a 404 status code when a resource is not found.')

    def test_get_single_resource_not_found(self):
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




