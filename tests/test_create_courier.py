import allure
import pytest
import requests
from data import Urls, CourierMessages
from helpers.courier_helper import generate_random_string, register_new_courier_and_return_login_password, delete_courier, get_courier_id



class TestCreateCourier:
    def test_create_courier_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/courier', data=payload)
  

        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        
        assert response.json() == CourierMessages.SUCCESS_CREATE, f"Ожидался {CourierMessages.SUCCESS_CREATE}, получен {response.json()}"
        
        courier_id = get_courier_id(login, password)
        if courier_id:
            delete_courier(courier_id)

    def test_create_duplicate_courier_fails(self):
        courier_data = register_new_courier_and_return_login_password()
        
        login = courier_data[0]
        password = courier_data[1]
        first_name = courier_data[2]
        
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/courier', data=payload)
        
        assert response.status_code == 409, f"Ожидался статус 409, получен {response.status_code}"
        
        assert CourierMessages.ERROR_DUPLICATE_LOGIN in response.json().get("message"), f"Ожидалось сообщение '{CourierMessages.ERROR_DUPLICATE_LOGIN}', получено {response.json().get('message')}"
        
        courier_id = get_courier_id(login, password)
        if courier_id:
            delete_courier(courier_id)

    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field_fails(self, missing_field):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        
        del payload[missing_field]
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/courier', data=payload)
        
        assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
        
        assert CourierMessages.ERROR_MISSING_FIELD in response.json().get("message"), f"Ожидалось сообщение '{CourierMessages.ERROR_MISSING_FIELD}', получено {response.json().get('message')}"
        
    @pytest.mark.parametrize("field_name", ["login", "password", "firstName"])
    def test_create_courier_empty_field_fails(self, field_name):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        payload[field_name] = ""
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/courier', data=payload)
        
        assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
        
    def test_create_courier_existing_login_fails(self, create_and_delete_courier):
        existing_courier = create_and_delete_courier
        
        payload = {
            "login": existing_courier["login"],
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/courier', data=payload)
        
        assert response.status_code == 409, f"Ожидался статус 409, получен {response.status_code}"
        
        assert CourierMessages.ERROR_DUPLICATE_LOGIN in response.json().get("message"), f"Ожидалось сообщение '{CourierMessages.ERROR_DUPLICATE_LOGIN}', получено {response.json().get('message')}"
