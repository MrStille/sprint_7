import pytest
from helpers.util import ApiHelper

@pytest.fixture(scope='function')
def random_courier():
    return {
        "login": ApiHelper.generate_random_string(10),
        "password": "Password123AP",
        "firstName": ApiHelper.generate_random_string(10)
    }

@pytest.fixture(scope='function')
def random_order():
    return {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }

def pytest_make_parametrize_id(config, val):
    return repr(val)