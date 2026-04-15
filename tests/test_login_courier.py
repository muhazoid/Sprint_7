import allure
import pytest
import requests
from data import Urls, CourierMessages
from helpers.courier_helper import generate_random_string, register_new_courier_and_return_login_password, delete_courier, get_courier_id


class TestLoginCourier:
     def test_login_courier_success(self):
        courier_data = register_new_courier_and_return_login_password()
        
        login = courier_data[0]
        password = courier_data[1]
        
        payload = {
            "login": login,
            "password": password
        }
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/courier/login', data=payload)
        
        assert response.status_code == 200
        
        assert "id" in response.json()
        
        courier_id = response.json().get("id")
        delete_courier(courier_id)


     def test_login_wrong_password_fails(self):
        courier_data = register_new_courier_and_return_login_password()
        
        login = courier_data[0]
         
        payload = {
            "login": login,
            "password": "password2345"
        }
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/courier/login', data=payload)

        assert response.status_code == 404
        assert CourierMessages.ERROR_AUTH_FAILED in response.json().get("message")
        
        correct_payload = {"login": login, "password": courier_data[1]}
        login_response = requests.post(f'{Urls.BASE_URL}/api/v1/courier/login', data=correct_payload)
        courier_id = login_response.json().get("id")
        delete_courier(courier_id)


     @pytest.mark.parametrize("missing_field", ["login", "password"])
     def test_login_missing_field_fails(self, missing_field):
        
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }
        del payload[missing_field]
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/courier/login', data=payload)
        
        assert response.status_code == 400
        
        assert CourierMessages.ERROR_MISSING_AUTH_FIELDS in response.json().get("message")
        

     @pytest.mark.parametrize("field_name", ["login", "password"])
     def test_login_empty_field_fails(self, field_name):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }
        payload[field_name] = ""
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/courier/login', data=payload)
        
        assert response.status_code == 400
        

     def test_login_nonexistent_login_fails(self):
        payload = {
            "login": "nonexistent_login_312122",
            "password": "password123"
        }
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/courier/login', data=payload)
        
        assert response.status_code == 404
        
        assert CourierMessages.ERROR_AUTH_FAILED in response.json().get("message")