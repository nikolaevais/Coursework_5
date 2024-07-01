import requests

class HHApi:
    """класс для подключения к API HH.ru"""
    def __get_request(self):
        """подключениe к API HH.ru и получение 10 популярных работадателей"""
        params = {'per_page': 10,
                  'sort_by': 'by_vacancies_open'}

        response = requests.get('https://api.hh.ru/employers', params=params)

        if response.status_code == 200:
            return response.json()['items']


    def get_employers(self):
        """сохранение списка работадателей"""
        employers = []
        data = self.__get_request()
        for employer in data:
            employers.append({"id": employer["id"], "name": employer["name"], "amount": employer["open_vacancies"]})
        return employers