import allure
import pytest
import requests
from data import Urls, CourierMessages
from helpers.courier_helper import generate_random_string, register_new_courier_and_return_login_password, delete_courier, get_courier_id


@allure.feature("Авторизация курьера")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    @allure.description("Проверяем, что курьер может авторизоваться с валидными данными")
    def test_login_courier_success(self, create_and_delete_courier):
        courier_data = create_and_delete_courier
        
        
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        
        with allure.step("Отправка POST-запроса на авторизацию курьера"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/courier/login', data=payload)
        
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
        
        with allure.step("Проверка наличия поля 'id' в ответе"):
            assert "id" in response.json(), "В ответе отсутствует поле 'id'"
                


    @allure.title("Авторизация с неверным паролем")
    @allure.description("Проверяем, что авторизация с неверным паролем возвращает ошибку")
    def test_login_wrong_password_fails(self, create_and_delete_courier):
        courier_data = create_and_delete_courier
         
        payload = {
            "login": courier_data["login"],
            "password": "password2345"
        }
        
        with allure.step(f"Отправка POST-запроса на авторизацию с неверным паролем"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/courier/login', data=payload)
        
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 404, f"Ожидался статус 404, получен {response.status_code}"
        
        with allure.step("Проверка сообщения об ошибке"):
            assert CourierMessages.ERROR_AUTH_FAILED in response.json().get("message"), f"Ожидалось сообщение '{CourierMessages.ERROR_AUTH_FAILED}', получено {response.json().get('message')}"


    @allure.title("Авторизация без обязательных полей")
    @allure.description("Проверяем, что авторизация без обязательных полей возвращает ошибку")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_field_fails(self, missing_field):
        
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }
        del payload[missing_field]
        
        with allure.step(f"Отправка POST-запроса на авторизацию без поля '{missing_field}'"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/courier/login', data=payload)
        
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
        
        with allure.step("Проверка сообщения об ошибке"):
            assert CourierMessages.ERROR_MISSING_AUTH_FIELDS in response.json().get("message"), f"Ожидалось сообщение '{CourierMessages.ERROR_MISSING_AUTH_FIELDS}', получено {response.json().get('message')}"
        

    @allure.title("Авторизация с пустыми полями")
    @allure.description("Проверяем, что авторизация с пустыми полями возвращает ошибку")
    @pytest.mark.parametrize("field_name", ["login", "password"])
    def test_login_empty_field_fails(self, field_name):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }
        payload[field_name] = ""
        
        with allure.step(f"Отправка POST-запроса на авторизацию с пустым полем '{field_name}'"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/courier/login', data=payload)
        
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
                

    @allure.title("Авторизация с несуществующим логином")
    @allure.description("Проверяем, что авторизация с несуществующим логином возвращает ошибку")
    def test_login_nonexistent_login_fails(self):
        payload = {
            "login": "nonexistent_login_312122",
            "password": "password123"
        }
        
        with allure.step("Отправка POST-запроса на авторизацию с несуществующим логином"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/courier/login', data=payload)
        
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 404, f"Ожидался статус 404, получен {response.status_code}"
        
        with allure.step("Проверка сообщения об ошибке"):
            assert CourierMessages.ERROR_AUTH_FAILED in response.json().get("message"), f"Ожидалось сообщение '{CourierMessages.ERROR_AUTH_FAILED}', получено {response.json().get('message')}"
                