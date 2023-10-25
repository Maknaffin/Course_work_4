from abc import ABC, abstractmethod
import requests


class API(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HHAPI(API):

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'only_with_salary': True, 'text': '', 'page': 0, 'per_page': 100}

    def get_vacancies(self, keyword):
        vacancies = []
        self.params['text'] = keyword
        while self.params['page'] != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            items = response.json()['items']
            vacancies.extend(items)
            self.params['page'] += 1
        return vacancies
