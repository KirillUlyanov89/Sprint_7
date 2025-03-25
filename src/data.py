# URL сервиса "Яндекс Самокат"
service_url = 'https://qa-scooter.praktikum-services.ru'

# URLы API для функциональности курьера
create_courier_url = service_url + '/api/v1/courier'
login_courier_url = service_url + '/api/v1/courier/login'
delete_courier_url = service_url + '/api/v1/courier/'

# Локаторы для функциональности курьера
CREATE_COURIER_DUPLICATION_ERROR_MESSAGE = 'Этот логин уже используется. Попробуйте другой.'
CREATE_COURIER_EMPTY_FIELD_ERROR_MESSAGE = 'Недостаточно данных для создания учетной записи'
LOGIN_WITH_INCORRECT_DATA_ERROR_MESSAGE = 'Учетная запись не найдена'
LOGIN_WITH_EMPTY_FIELD_ERROR_MESSAGE = 'Недостаточно данных для входа'
DELETE_WITH_EMPTY_ID_ERROR_MESSAGE = 'Недостаточно данных для удаления курьера'
DELETE_WITH_UNEXISTING_ID_ERROR_MESSAGE = 'Курьера с таким id нет.'

# URLы API для функциональности заказов
create_order_url = service_url + '/api/v1/orders'
get_orders_url = service_url + '/api/v1/orders'

# Данные для тестовых заказов
ORDER_INFO_NO_COLOR = {
    "firstName": "Kot",
    "lastName": "Kotiauzer",
    "address": "Lenina, 142 ",
    "metroStation": 4,
    "phone": "+7 999 999 99 99",
    "rentTime": 5,
    "deliveryDate": "2025-04-04",
    "comment": "Не звонить",
    "color": []
    }

ORDER_INFO_COLOR_BLACK = {
    "firstName": "Kot",
    "lastName": "Kotiauzer",
    "address": "Lenina, 142 ",
    "metroStation": 4,
    "phone": "+7 999 999 99 99",
    "rentTime": 5,
    "deliveryDate": "2025-04-04",
    "comment": "Не звонить",
    "color": ["BLACK"]
    }

ORDER_INFO_COLOR_GREY = {
    "firstName": "Kot",
    "lastName": "Kotiauzer",
    "address": "Lenina, 142 ",
    "metroStation": 4,
    "phone": "+7 999 999 99 99",
    "rentTime": 5,
    "deliveryDate": "2025-04-04",
    "comment": "Не звонить",
    "color": ["GRAY"]
    }

ORDER_INFO_COLOR_BLACK_AND_GREY = {
    "firstName": "Kot",
    "lastName": "Kotiauzer",
    "address": "Lenina, 142 ",
    "metroStation": 4,
    "phone": "+7 999 999 99 99",
    "rentTime": 5,
    "deliveryDate": "2025-04-04",
    "comment": "Не звонить",
    "color": ["BLACK", "GREY"]
    }