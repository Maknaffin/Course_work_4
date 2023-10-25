from abc import ABC, abstractmethod
import requests
import os


class API(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HHAPI(API):

    def __init__(self):
        self.hh_api_url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'only_with_salary': True, 'text': '', 'page': 0, 'per_page': 100}

    def get_vacancies(self, keyword):
        vacancies = []
        self.params['text'] = keyword
        while self.params['page'] != 5:
            response = requests.get(self.hh_api_url, headers=self.headers, params=self.params)
            items = response.json()['items']
            vacancies.extend(items)
            self.params['page'] += 1
        return vacancies


class SJAPI(API):

    def __init__(self):
        self.sj_api_url = 'https://api.superjob.ru/2.0/vacancies'
        self.SJ_API_TOKEN = os.getenv("SJ_TOKEN")
        self.headers = {"X-Api-App-Id": self.SJ_API_TOKEN}
        self.params = {'keyword': '', 'count': 100, 'page': 0}

    def get_vacancies(self, keyword):
        vacancies = []
        self.params['keyword'] = keyword
        while self.params['page'] != 5:
            response = requests.get(self.sj_api_url, headers=self.headers, params=self.params)
            items = response.json()['objects']
            vacancies.extend(items)
            self.params['page'] += 1
        return vacancies
