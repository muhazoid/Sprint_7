import requests
import random
import string
from data import Urls
import allure


@allure.step("Регистрация нового курьера и возврат логина/пароля")
def register_new_courier_and_return_login_password():
    
    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass

@allure.step("Удаление курьера по ID")
def delete_courier(courier_id):
    response = requests.delete(f'{Urls.BASE_URL}/api/v1/courier/{courier_id}')
    return response

allure.step("Получение ID курьера по логину и паролю")
def get_courier_id(login, password):
    payload = {
        "login": login,
        "password": password
    }
    response = requests.post(f'{Urls.BASE_URL}/api/v1/courier/login', data=payload)
    return response.json().get("id")

@allure.step("Генерация случайной строки длиной {length}")
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string