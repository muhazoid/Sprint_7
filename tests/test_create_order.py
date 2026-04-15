import allure
import pytest
import requests
from data import Urls, OrderData



class TestCreateOrder:  
    
    @pytest.mark.parametrize("order_template", [OrderData.BASE_ORDER, OrderData.ALTERNATIVE_ORDER])
    def test_create_order_with_different_data(self, order_template):
        payload = order_template.copy()
        payload["color"] = OrderData.COLORS["BLACK"]
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/orders', json=payload)
        
        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        assert "track" in response.json(), "В ответе отсутствует поле 'track'"
        assert response.json()["track"] is not None, "Значение track не должно быть пустым"


    def test_create_order_with_empty_json(self):
        payload = {}
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/orders', json=payload)
        
        assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
        
    
    def test_create_order_without_color(self):
        payload = OrderData.BASE_ORDER.copy()
        payload["color"] = OrderData.COLORS["NONE"]
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/orders', json=payload)
        
        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        assert "track" in response.json(), "В ответе отсутствует поле 'track'"
        assert response.json()["track"] is not None, "Значение track не должно быть пустым"


    def test_create_order_with_black_color(self):
        payload = OrderData.BASE_ORDER.copy()
        payload["color"] = OrderData.COLORS["BLACK"]
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/orders', json=payload)
        
        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        assert "track" in response.json(), "В ответе отсутствует поле 'track'"
        assert response.json()["track"] is not None, "Значение track не должно быть пустым"
    
    def test_create_order_with_grey_color(self):
        payload = OrderData.BASE_ORDER.copy()
        payload["color"] = OrderData.COLORS["GREY"]
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/orders', json=payload)
        
        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        assert "track" in response.json(), "В ответе отсутствует поле 'track'"
        assert response.json()["track"] is not None, "Значение track не должно быть пустым"
    
    def test_create_order_with_both_colors(self):
        payload = OrderData.BASE_ORDER.copy()
        payload["color"] = OrderData.COLORS["BOTH"]
        
        response = requests.post(f'{Urls.BASE_URL}/api/v1/orders', json=payload)
        
        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
        assert "track" in response.json(), "В ответе отсутствует поле 'track'"
        assert response.json()["track"] is not None, "Значение track не должно быть пустым"