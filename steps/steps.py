import json

import allure

import requests

from data import Data
from helpers.log import ApiLog


class Steps:

    @staticmethod
    @allure.step('Регистрация нового пользователя')
    def create_courier(courier):
        route_url = Data.API_URL + '/courier'
        response = requests.post(route_url, data=courier)
        ApiLog.log_req(route_url, response)
        return response

    @staticmethod
    @allure.step('Логин пользователя пользователя')
    def login_courier(courier):
        route_url = Data.API_URL + '/courier/login'
        payload = {
            "login": courier.get("login"),
            "password": courier.get("password"),
        }
        response = requests.post(route_url, data=payload)
        ApiLog.log_req(route_url, response)
        return response


    @staticmethod
    @allure.step('Создание заказа')
    def create_order(order):
        route_url = Data.API_URL + '/orders'
        response = requests.post(route_url, data=json.dumps(order))
        ApiLog.log_req(route_url, response)
        return response


    @staticmethod
    @allure.step('Получить список всех заказов')
    def get_all_orders():
        route_url = Data.API_URL + '/orders'
        response = requests.get(route_url)
        ApiLog.log_req(route_url, response)
        assert response.status_code == 200
        return response.json()

    @staticmethod
    @allure.step('Удаляем курьера')
    def delete_courier(courier):
        login_courier = Steps.login_courier(courier)
        assert login_courier.status_code == 200
        courier_id = login_courier.json()['id']
        route_url = Data.API_URL + '/courier/' + str(courier_id)
        response = requests.delete(route_url)
        ApiLog.log_req(route_url, response)
        assert response.status_code == 200

    @staticmethod
    @allure.step('Удаляем курьера по id')
    def delete_courier_by_id(courier_id):
        route_url = Data.API_URL + '/courier/' + str(courier_id)
        response = requests.delete(route_url)
        ApiLog.log_req(route_url, response)
        assert response.status_code == 200
