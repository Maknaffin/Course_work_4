from abc import ABC, abstractmethod
import json


class JSON(ABC):

    @abstractmethod
    def save_vacancies(self, vacancy_list, filename):
        pass

    @abstractmethod
    def load_vacancies(self, filename):
        pass


class JSONSaver(JSON):
    """Класс для обработки списка вакансий в json формате"""

    def save_vacancies(self, vacancy_list, filename):
        """Сохранение вакансий в json"""
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(vacancy_list, file, indent=2, ensure_ascii=False)

    def load_vacancies(self, filename):
        """Получение вакансий из json"""
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
