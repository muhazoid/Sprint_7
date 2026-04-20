import pytest
from helpers.courier_helper import register_new_courier_and_return_login_password, delete_courier, get_courier_id, generate_random_string
from data import Urls
import requests

@pytest.fixture
def create_and_delete_courier():
    courier_data = register_new_courier_and_return_login_password()
    
    login, password, first_name = courier_data
    
    yield {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    courier_id = get_courier_id(login, password)
    if courier_id:
        delete_courier(courier_id)

@pytest.fixture
def create_and_delete_courier_with_response():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    response = requests.post(f'{Urls.BASE_URL}/api/v1/courier', data=payload)
    
    yield {
        "response": response,
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    courier_id = get_courier_id(login, password)
    if courier_id:
        delete_courier(courier_id)