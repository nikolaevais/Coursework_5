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

    def __get_vacancies_on_employer(self, id):
        """подключениe к API HH.ru и получение вакансий 10 популярных работадателей"""
        params = {"employer_id": id}
        response = requests.get("https://api.hh.ru/vacancies", params=params)
        if response.status_code == 200:
            return response.json()["items"]



    def get_all_vacancies(self):
        """сохранение списка вакансий"""
        employers = self.get_employers()
        all_vacancies = []
        for employer in employers:
            vacancies = self.__get_vacancies_on_employer(employer["id"])
            for vacancy in vacancies:
                if vacancy["salary"] is None:
                    salary_from = 0
                    salary_to = 0
                else:
                    salary_from = vacancy["salary"]["from"] if vacancy["salary"]["from"] else 0
                    salary_to = vacancy["salary"]["to"] if vacancy["salary"]["to"] else 0
                all_vacancies.append({"id": vacancy["id"],
                                      "name": vacancy["name"],
                                      "url": vacancy["alternate_url"],
                                      "salary_from": salary_from,
                                      "salary_to": salary_to,
                                      "employer": employer["id"],
                                      "area": vacancy["area"]["name"]})
        return all_vacancies