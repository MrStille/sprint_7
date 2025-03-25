import allure
import pytest

from steps.steps import Steps

@allure.epic('Заказы')
class TestOrder:

    @allure.title("Создаем новый заказ")
    def test_create_order(self, random_order):
        response = Steps.create_order(random_order)
        assert response.status_code == 201
        assert response.json()['track'] > 0

    @allure.title("Создаем заказы с разными параметрами цвета")
    @pytest.mark.parametrize('field, value',
                             [
                                 ["color", ["BlACK","GREY"]],
                                 ["color", ["GREY"]],
                                 ["color", []],
                             ])
    def test_create_order(self, random_order, field, value):
        response = Steps.create_order(random_order)
        assert response.status_code == 201
        assert response.json()['track'] > 0

    @allure.title("Получить  список всех заказов")
    def test_get_order_list(self):
        orders_lst = Steps.get_all_orders()
        assert len(orders_lst) > 0
        assert orders_lst['orders'][0]['id'] > 0
        assert orders_lst['orders'][0]['track'] > 0
        assert orders_lst['pageInfo']["total"] > 0