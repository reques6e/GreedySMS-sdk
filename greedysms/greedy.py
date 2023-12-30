import aiohttp

class GreedyAPI:
    def __init__(self, token):
        """Параметры для всех запросов"""
        self.base_url = 'https://greedyapi.ru'
        self.headers = {'Authorization': f'Bearer {token}'}
        self.session = aiohttp.ClientSession()

    async def get_me(self):
        """Получение информации о пользователе"""
        endpoint = 'getMe'
        response = await self.send_request(endpoint)
        return await response.json()
         
    async def buy_number(self, service_id, country_id):
        """Покупка номера"""
        endpoint = 'buyNumber'
        params = {'service': service_id, 'country': country_id}
        response = await self.send_request(endpoint, method='GET', params=params)
        return await response.json()

    async def get_status(self, operation_id):
        """Получение статуса"""
        endpoint = 'getStatus'
        params = {'operation_id': operation_id}
        response = await self.send_request(endpoint, params=params)
        return await response.json()
    
    async def set_status(self, operation_id, status):
        """Изменение статуса"""
        endpoint = 'setStatus'
        params = {'operation_id': operation_id, 'status': status}
        response = await self.send_request(endpoint, params=params)
        return await response.json()
    
    async def get_price(self, service_id, country_id):
        """Получение цены на номер"""
        endpoint = 'getPrice'
        params = {'service': service_id, 'country': country_id}
        response = await self.send_request(endpoint, params=params)
        return await response.json()

    async def get_prices(self, country_id):
        """ Получение цен на все сервисы"""
        endpoint = 'getPrices'
        params = {'country': country_id}
        response = await self.send_request(endpoint, params=params)
        return await response.json()

    async def get_count_numbers(self, country_id):
        """Получение количества номеров на сервисах."""
        endpoint = 'getCountNumbers'
        params = {'country': country_id}
        response = await self.send_request(endpoint, params=params)
        return await response.json()
    
    async def send_request(self, endpoint, method='GET', data=None, params=None):
        """Отправка запросов"""
        url = f'{self.base_url}/{endpoint}'
        async with self.session.request(method, url, json=data, params=params, headers=self.headers) as response:
            return response
