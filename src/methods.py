class Methods:
    """Класс для валидации данных"""

    def get_all_vacancies(self, list_vacancies):
        """Получение всех вакансий"""
        for item in list_vacancies:
            return f"{item.title}\n{item.salary}\n{item.description}\n{item.currency}\n"

    def get_top_n_vacancies(self, number_user, list_vacancies):
        """Получение топ N вакансий"""
        final_sorted = sorted(list_vacancies, key=lambda d: d.salary, reverse=True)
        items = final_sorted[:number_user]
        for item in items:
            return f"{item.title}\n{item.salary}\n{item.description}\n{item.currency}\n"

    def get_key_word(self, keyword, list_vacancies):
        """Получение вакансий по ключевому слову"""
        items = []
        for vacancy in list_vacancies:
            if vacancy.description and keyword in vacancy.description:
                items.append(vacancy)

        for item in items:
            return f"{item.title}\n{item.salary}\n{item.description}\n{item.currency}\n"
