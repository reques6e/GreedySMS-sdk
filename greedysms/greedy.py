### SDK НЕ ОФИЦИАЛЬНЫЙ

import requests

class GreedyAPI:
    def __init__(self, token):
        """Параметры для всех запросов"""
        self.base_url = 'https://greedyapi.ru'
        self.headers = {'Authorization': f'Bearer {token}'}

    def get_me(self):
        """Получение информации о пользователе"""
        endpoint = 'getMe'

        response = self.send_request('GET', endpoint)
        return response.json()
         
    def buy_number(self, service_id, country_id):
        """Покупка номера"""
        endpoint = 'buyNumber'
        params = {'service': service_id, 'country': country_id}

        response = self.send_request('GET', endpoint, params=params)
        return response.json()

    def get_status(self, operation_id):
        """Получение статуса"""
        endpoint = 'getStatus'
        params = {'operation_id': operation_id}
        response = self.send_request('GET', endpoint, params=params)
        return response.json()
    
    def set_status(self, operation_id, status):
        """Изменение статуса"""
        endpoint = 'setStatus'
        params = {'operation_id': operation_id, 'status': status}
        response = self.send_request('GET', endpoint, params=params)
        return response.json()
    
    def get_price(self, service_id, country_id):
        """Получение цены на номер"""
        endpoint = 'getPrice'
        params = {'service': service_id, 'country': country_id}
        response = self.send_request('GET', endpoint, params=params)
        return response.json()

    def get_prices(self, country_id):
        """ Получение цен на все сервисы"""
        endpoint = 'getPrices'
        params = {'country': country_id}
        response = self.send_request('GET', endpoint, params=params)
        return response.json()

    def get_count_numbers(self, country_id):
        """Получение количества номеров на сервисах."""
        endpoint = 'getCountNumbers'
        params = {'country': country_id}
        response = self.send_request('GET', endpoint, params=params)
        return response.json()
    
    def send_request(self, method, endpoint, data=None, params=None):
        """Отправка запросов"""
        url = f'{self.base_url}/{endpoint}'
        response = requests.request(method, url, json=data, params=params, headers=self.headers)
        return response
