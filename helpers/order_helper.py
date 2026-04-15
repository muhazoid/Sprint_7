import requests
from data import Urls, OrderData
import allure


class Orders:

        @staticmethod
        def create_test_order():
                payload = OrderData.BASE_ORDER.copy()
              
                response = requests.post(f'{Urls.BASE_URL}/api/v1/orders', json=payload)
                return response.json().get("track")