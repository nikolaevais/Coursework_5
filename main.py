from src.utils import create_database, create_tables, insert_data_in_tables
from src.DBManager import DBManager


db_name = "coursework_5"
create_database(db_name)
create_tables(db_name)
insert_data_in_tables(db_name)

db = DBManager("coursework_5")

while True:
    print("""Для получения информации выберите следующее действие:
            1 - получить список всех компаний и количество вакансий у каждой компании
            2 - получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
            3 - получить среднюю зарплату по вакансиям
            4 - получить список всех вакансий, у которых зарплата выше средней по всем вакансиям
            5 - получить список выбранных вакансий
            6 - выйти из программы""")
    user_answer = input()
    if user_answer == "1":
        print(db.get_companies_and_vacancies_count())
    elif user_answer == "2":
        print(db.get_all_vacancies())
    elif user_answer == "3":
        print(db.get_avg_salary())
    elif user_answer == "4":
        print(db.get_vacancies_with_higher_salary())
    elif user_answer == "5":
        print("Введите название вакансии")
        user_answer_vacancy = input()
        print(db.get_vacancies_with_keyword(f"{user_answer_vacancy}"))
    elif user_answer == "6":
        break