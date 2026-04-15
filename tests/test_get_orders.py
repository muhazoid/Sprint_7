import allure
import pytest
import requests
from data import Urls



class TestGetOrders:
    
    def test_get_orders_without_params(self):
        response = requests.get(f'{Urls.BASE_URL}/api/v1/orders')
        
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
        assert "orders" in response.json(), "В ответе отсутствует поле 'orders'"
        assert isinstance(response.json()["orders"], list), "Поле 'orders' должно быть списком"
        
    