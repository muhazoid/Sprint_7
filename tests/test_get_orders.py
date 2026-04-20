import allure
import requests
from data import Urls
from helpers.order_helper import Orders


@allure.feature("Получение заказов")
class TestGetOrders:
    
    @allure.title("Получение списка заказов без параметров")
    @allure.description("Проверяем, что можно получить список заказов и статус код 200")
    def test_get_orders_without_params_success(self):
        
        with allure.step("Создание тестового заказа для гарантии наличия данных"):
            Orders.create_test_order()
        
        with allure.step("Отправка GET-запроса на получение списка заказов"):
            response = requests.get(f'{Urls.BASE_URL}/api/v1/orders')
        
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
                
        with allure.step("Проверка наличия поля 'orders' в ответе"):
            assert "orders" in response.json(), "В ответе отсутствует поле 'orders'"
        
        with allure.step("Проверка, что поле 'orders' является списком"):
            assert isinstance(response.json()["orders"], list), "Поле 'orders' должно быть списком"
        
    