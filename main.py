from src.api import HHAPI
from src.utils import vacancies_instanse
from src.json_manager import JSONSaver
from src.methods import Methods


def user_interaction():
    print(f"Привет! Я программа для сбора информации о вакансиях! Приступим!\n")
    while True:
        platform_input = input(f"Выбери платформу:\n1 - HeadHunter\n2 - SuperJob\n0 - Выйти\n> ")
        if platform_input not in ["0", "1", "2"]:
            print(f"Упс. Кажется в моей базе нет такой платформы. Попробуй еще раз!")
            print()
        else:
            platform = {
                "1": "HeadHunter",
                "2": "SuperJob"
            }
            if platform_input == "0":
                print("Всего хорошего!")
                break
            else:
                print(f"Отлично! Ты выбрал платформу {platform[platform_input]}\n")
                input_prof = input(f"Теперь введи название профессии:\n> ").capitalize()
                if platform_input == "1":
                    hh = HHAPI()
                    hh_vacancies = hh.get_vacancies(input_prof)  # Получение вакансий с HeadHunter

                if platform_input == "2":
                    pass

            # Сохранение информации о вакансиях в файл
            filename = "vacancies.json"

            json_saver = JSONSaver()
            json_saver.save_vacancies(hh_vacancies, filename)
            data = json_saver.load_vacancies(filename)

            # Сортировка вакансий по названию, описанию и зарплате
            raws = vacancies_instanse(data)

            # Вывод операций над списком вакансий
            method_chosen = input(f"Выберите следующие действия:\n"
                                  f"1 - Вывести весь список вакансий\n"
                                  f"2 - Вывести топ N вакансий (по убыванию)\n"
                                  f"3 - Найти вакансию по ключевому слову\n"
                                  f"0 - Вернуться к выбору платформы и вакансий (выйти)\n> ")
            methods = Methods()

            # Вывод всего списка вакансий
            if method_chosen == "1":
                vacancy = methods.get_all_vacancies(raws)
                print(vacancy)
                break

            # Вывод топ N вакансий
            if method_chosen == "2":
                n_input = int(input(f"Введите желаемое количество вакансий для "
                                    f"обработки:\n> "))
                vacancy = methods.get_top_n_vacancies(n_input, raws)
                print(vacancy)
                break

            # Вывод вакансии по ключевому слову
            if method_chosen == "3":
                keyword_input = input(f"Введите ключевое слово: \n> ")
                vacancy = methods.get_key_word(keyword_input, raws)
                if vacancy:
                    print(vacancy)
                else:
                    print(f"Упс. Кажется такого слова нет ни в одном описании найденных вакансии")
                break

            # Возвращение к выбору платформы
            if method_chosen == "0":
                continue


if __name__ == "__main__":
    user_interaction()
