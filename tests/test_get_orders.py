import allure
import pytest
import requests
from data import Urls
from helpers.order_helper import Orders


@allure.feature("Получение заказов")
class TestGetOrders:
    
    @allure.title("Получение списка заказов без параметров")
    @allure.description("Проверяем, что можно получить список заказов и статус код 200")
    def test_get_orders_without_params_success(self):
        Orders.create_test_order()
        response = requests.get(f'{Urls.BASE_URL}/api/v1/orders')
        
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
        assert "orders" in response.json(), "В ответе отсутствует поле 'orders'"
        assert isinstance(response.json()["orders"], list), "Поле 'orders' должно быть списком"
        
    