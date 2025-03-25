import allure
import pytest

from helpers.util import ApiHelper
from steps.steps import Steps

@allure.epic('Create - login courier')
class TestCourier:

    @allure.title("Регистрация нового курьера")
    def test_register_new_courier(self, random_courier):
        response = Steps.create_courier(random_courier)
        assert response.status_code == 201
        assert response.json()["ok"] == True

    @allure.title("Нельзя зарегистрировать курьера с ошибочными данным")
    @pytest.mark.parametrize('field, value,expected_code, error',
                             [
                                 ["login", "", 400, "Недостаточно данных для создания учетной записи"],
                                 ["password", "", 400, "Недостаточно данных для создания учетной записи"],
                             ])
    def test_register_new_courier_negative(self, random_courier, field, value, expected_code, error):
        random_courier[field] = value
        response = Steps.create_courier(random_courier)
        js = response.json()
        assert response.status_code == expected_code
        assert js["message"] == error

    @allure.title("Нельзя создать курьера с один и тем же логином")
    def test_cannot_create_courier_with_same_login(self, random_courier):
        response_courier1 = Steps.create_courier(random_courier)
        assert response_courier1.status_code == 201
        response_courier2 = Steps.create_courier(random_courier)
        assert response_courier2.status_code == 409

    @allure.title("Новой курьер может войти в систему")
    def test_login_courier(self, random_courier):
        courier = ApiHelper.random_courier()
        response_create = Steps.create_courier(courier)
        assert response_create.status_code == 201
        assert response_create.json()["ok"] == True
        response = Steps.login_courier(courier)
        assert response.status_code == 200
        assert response.json()["id"] > 0

    @allure.title("Нельзя зарегистрировать курьера с ошибочными данным")
    @pytest.mark.parametrize('field, value,expected_code, error',
                             [
                                 ["login", "", 400, "Недостаточно данных для входа"],
                                 ["password", "", 400, "Недостаточно данных для входа"],
                                 ["password", "wrongPass", 404, "Учетная запись не найдена"],
                             ])
    def test_login_courier_negative(self, random_courier, field, value, expected_code, error):
        response = Steps.create_courier(random_courier)
        assert response.status_code == 201
        user = random_courier.copy()
        user[field] = value
        response = Steps.login_courier(user)
        js = response.json()
        assert response.status_code == expected_code
        assert js["message"] == error
