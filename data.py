class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"


class CourierMessages:
    ERROR_MISSING_FIELD = "Недостаточно данных для создания учетной записи"
    ERROR_DUPLICATE_LOGIN = "Этот логин уже используется"
    ERROR_AUTH_FAILED = "Учетная запись не найдена"
    ERROR_MISSING_AUTH_FIELDS = "Недостаточно данных для входа"
    
    SUCCESS_CREATE = {"ok": True}

class OrderData:
    COLORS = {
        "BLACK": ["BLACK"],
        "GREY": ["GREY"],
        "BOTH": ["BLACK", "GREY"],
        "NONE": []
    }
    
    BASE_ORDER = {
        "firstName": "Алексей",
        "lastName": "Алексеич",
        "address": "Новокузнецк",
        "metroStation": 1,
        "phone": "+79001234567",
        "rentTime": 5,
        "deliveryDate": "2026-04-16",
        "comment": "Тестовый заказ"
    }
    
    ALTERNATIVE_ORDER = {
        "firstName": "Ольга",
        "lastName": "Ольгович",
        "address": "пр. Новокузнецк, д. 5",
        "metroStation": 5,
        "phone": "+79109876543",
        "rentTime": 3,
        "deliveryDate": "2026-04-17",
        "comment": "Позвонить за час"
    }