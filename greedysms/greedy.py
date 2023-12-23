### SDK НЕ ОФИЦИАЛЬНЫЙ

import requests

class GreedyAPI:
    def __init__(self, token):
        self.base_url = 'https://greedyapi.ru'

        # Параметры для всех запросов
        self.headers = {'Authorization': f'Bearer {token}'}

     def get_me(self):
        endpoint = 'getMe'

        response = self.send_request('GET', endpoint)
        return response.json()
         
    def buy_number(self, service_id, country_id):
        endpoint = 'buyNumber'
        params = {'service': service_id, 'country': country_id}

        response = self.send_request('GET', endpoint, params=params)
        return response.json()

    def get_status(self, operation_id):
        endpoint = 'getStatus'
        params = {'operation_id': operation_id}
        response = self.send_request('GET', endpoint, params=params)
        return response.json()
    
    def set_status(self, operation_id, status):
        endpoint = 'setStatus'
        params = {'operation_id': operation_id, 'status': status}
        response = self.send_request('GET', endpoint, params=params)
        return response.json()
    
    def get_price(self, service_id, country_id):
        endpoint = 'getPrice'
        params = {'service': service_id, 'country': country_id}
        response = self.send_request('GET', endpoint, params=params)
        return response.json()

    def get_prices(self, country_id):
        endpoint = 'getPrices'
        params = {'country': country_id}
        response = self.send_request('GET', endpoint, params=params)
        return response.json()

    def get_count_numbers(self, country_id):
        endpoint = 'getCountNumbers'
        params = {'country': country_id}
        response = self.send_request('GET', endpoint, params=params)
        return response.json()
    
    def send_request(self, method, endpoint, data=None, params=None):
        url = f'{self.base_url}/{endpoint}'
        response = requests.request(method, url, json=data, params=params, headers=self.headers)
        return response
