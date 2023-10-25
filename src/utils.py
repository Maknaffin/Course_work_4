from src.vacancy import Vacancy


def vacancies_instanse_hh(raw_vacancies):
    """Создание списка экземпляров класса Vacancy"""
    vacancies = []
    for raw_vacancy in raw_vacancies:
        if raw_vacancy.get('name') and raw_vacancy['salary']['currency'] == "RUR":
            vacancy = Vacancy(raw_vacancy['name'], raw_vacancy['snippet']['requirement'],
                              raw_vacancy['salary']['currency'], raw_vacancy['salary']['from'])
        else:
            pass
        vacancies.append(vacancy)
    return vacancies

def vacancies_instanse_sj(raw_vacancies):
    """Создание списка экземпляров класса Vacancy"""
    vacancies = []
    for raw_vacancy in raw_vacancies:
        if raw_vacancy.get('profession') and raw_vacancy['currency'] == "rub":
            vacancy = Vacancy(raw_vacancy['profession'], raw_vacancy['candidat'],
                              raw_vacancy['currency'], raw_vacancy['payment_from'])
        else:
            pass
        vacancies.append(vacancy)
    return vacancies
