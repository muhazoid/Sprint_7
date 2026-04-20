import allure
import pytest
import requests
from data import Urls, CourierMessages
from helpers.courier_helper import generate_random_string, register_new_courier_and_return_login_password, delete_courier, get_courier_id


@allure.feature("Создание курьера")
class TestCreateCourier:
    
    @allure.title("Успешное создание курьера")
    @allure.description("Проверяем, что курьер создается с валидными данными")
    def test_create_courier_success(self, create_and_delete_courier_with_response):
        response = create_and_delete_courier_with_response["response"]
    
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
    
        with allure.step("Проверка тела ответа"):
            assert response.json() == CourierMessages.SUCCESS_CREATE, f"Ожидался {CourierMessages.SUCCESS_CREATE}, получен {response.json()}"
            

    @allure.title("Создание дубликата курьера")
    @allure.description("Проверяем, что нельзя создать двух курьеров с одинаковыми данными")
    def test_create_duplicate_courier_fails(self, create_and_delete_courier):
        login = create_and_delete_courier["login"]
        password = create_and_delete_courier["password"]
        first_name = create_and_delete_courier["firstName"]
        
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        
        with allure.step("Отправка POST-запроса на создание дубликата курьера"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/courier', data=payload)
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 409, f"Ожидался статус 409, получен {response.status_code}"
        with allure.step("Проверка сообщения об ошибке"):
            assert CourierMessages.ERROR_DUPLICATE_LOGIN in response.json().get("message"), f"Ожидалось сообщение '{CourierMessages.ERROR_DUPLICATE_LOGIN}', получено {response.json().get('message')}"
        


    @allure.title("Создание курьера без обязательного поля")
    @allure.description("Проверяем, что нельзя создать  курьера без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field_fails(self, missing_field):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        
        del payload[missing_field]
        
        with allure.step(f"Отправка POST-запроса на создание курьера без поля '{missing_field}'"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/courier', data=payload)
    
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
    
        with allure.step("Проверка сообщения об ошибке"):
            assert CourierMessages.ERROR_MISSING_FIELD in response.json().get("message"), f"Ожидалось сообщение '{CourierMessages.ERROR_MISSING_FIELD}', получено {response.json().get('message')}"
            

    @allure.title("Создание курьера с пустым обязательным полем")
    @allure.description("Проверяем, что нельзя создать  курьера с пустым обязательным полем")    
    @pytest.mark.parametrize("field_name", ["login", "password", "firstName"])
    def test_create_courier_empty_field_fails(self, field_name):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        payload[field_name] = ""
        
        with allure.step(f"Отправка POST-запроса на создание курьера с пустым полем '{field_name}'"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/courier', data=payload)
    
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
            


    @allure.title("Создание курьера с уже используемым логином")
    @allure.description("Проверяем, что нельзя создать  курьера с существующим логином")
    def test_create_courier_existing_login_fails(self, create_and_delete_courier):
        existing_courier = create_and_delete_courier
        
        payload = {
            "login": existing_courier["login"],
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        
        with allure.step(f"Отправка POST-запроса на создание курьера с существующим логином '{existing_courier['login']}'"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/courier', data=payload)
    
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 409, f"Ожидался статус 409, получен {response.status_code}"
    
        with allure.step("Проверка сообщения об ошибке"):
            assert CourierMessages.ERROR_DUPLICATE_LOGIN in response.json().get("message"), f"Ожидалось сообщение '{CourierMessages.ERROR_DUPLICATE_LOGIN}', получено {response.json().get('message')}"
            
