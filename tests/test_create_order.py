import allure
import pytest
import requests
from data import Urls, OrderData


@allure.feature("Создание заказа")
class TestCreateOrder:  

    @allure.title("Создание заказа с разными наборами данных")
    @allure.description("Проверяем, что можно создать заказ с разными наборами данных")
    @pytest.mark.parametrize("order_template", [OrderData.BASE_ORDER, OrderData.ALTERNATIVE_ORDER])
    def test_create_order_with_different_data_success(self, order_template):
        payload = order_template.copy()
        payload["color"] = OrderData.COLORS["BLACK"]
        
        with allure.step("Отправка POST-запроса на создание заказа"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/orders', json=payload)
        
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
                
        with allure.step("Проверка наличия поля 'track' в ответе"):
            assert "track" in response.json(), "В ответе отсутствует поле 'track'"
                
        with allure.step("Проверка, что значение track не пустое"):
            assert response.json()["track"] is not None, "Значение track не должно быть пустым"
                


    @allure.title("Создание заказа с пустым телом запроса")
    @allure.description("Проверяем, что нельзя создать заказ с пустым телом запроса")
    def test_create_order_with_empty_json_fails(self):
        payload = {}
        
        with allure.step("Отправка POST-запроса с пустым телом"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/orders', json=payload)
        
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
        

    @allure.title("Создание заказа без указания цвета")
    @allure.description("Проверяем, что можно создать заказ без указания цвета")
    def test_create_order_without_color_success(self):
        payload = OrderData.BASE_ORDER.copy()
        payload["color"] = OrderData.COLORS["NONE"]
        
        with allure.step("Отправка POST-запроса на создание заказа без указания цвета"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/orders', json=payload)
        
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        
        with allure.step("Проверка наличия поля 'track' в ответе"):
            assert "track" in response.json(), "В ответе отсутствует поле 'track'"
        
        with allure.step("Проверка, что значение track не пустое"):
            assert response.json()["track"] is not None, "Значение track не должно быть пустым"


    @allure.title("Создание заказа с цветом BLACK")
    @allure.description("Проверяем, что можно создать заказ с цветом BLACK")
    def test_create_order_with_black_color_success(self):
        payload = OrderData.BASE_ORDER.copy()
        payload["color"] = OrderData.COLORS["BLACK"]
        
        with allure.step("Отправка POST-запроса на создание заказа с цветом BLACK"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/orders', json=payload)
        
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        
        with allure.step("Проверка наличия поля 'track' в ответе"):
            assert "track" in response.json(), "В ответе отсутствует поле 'track'"
        
        with allure.step("Проверка, что значение track не пустое"):
            assert response.json()["track"] is not None, "Значение track не должно быть пустым"
                
    

    @allure.title("Создание заказа с цветом GREY")
    @allure.description("Проверяем, что можно создать заказ с цветом GREY")
    def test_create_order_with_grey_color_success(self):
        payload = OrderData.BASE_ORDER.copy()
        payload["color"] = OrderData.COLORS["GREY"]
        
        with allure.step("Отправка POST-запроса на создание заказа с цветом GREY"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/orders', json=payload)
        
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        
        with allure.step("Проверка наличия поля 'track' в ответе"):
            assert "track" in response.json(), "В ответе отсутствует поле 'track'"
        
        with allure.step("Проверка, что значение track не пустое"):
            assert response.json()["track"] is not None, "Значение track не должно быть пустым"


    @allure.title("Создание заказа с двумя цветами")
    @allure.description("Проверяем, что можно создать заказ с двумя цветами")
    def test_create_order_with_both_colors_success(self):
        payload = OrderData.BASE_ORDER.copy()
        payload["color"] = OrderData.COLORS["BOTH"]
        
        with allure.step("Отправка POST-запроса на создание заказа с двумя цветами (BLACK и GREY)"):
            response = requests.post(f'{Urls.BASE_URL}/api/v1/orders', json=payload)
        
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        
        with allure.step("Проверка наличия поля 'track' в ответе"):
            assert "track" in response.json(), "В ответе отсутствует поле 'track'"
        
        with allure.step("Проверка, что значение track не пустое"):
            assert response.json()["track"] is not None, "Значение track не должно быть пустым"