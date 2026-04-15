import pytest
import requests
from helpers.courier_helper import register_new_courier_and_return_login_password, delete_courier, get_courier_id
from data import Urls


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