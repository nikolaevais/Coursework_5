mport os
import dotenv

dotenv.load_dotenv()

class DBManager:
    def __init__(self, name):
        self.__name = name

    def __execute_query(self, query):
        """подключение к базе данных"""
        conn = psycopg2.connect(dbname=self.__name, user=os.getenv("user"),
                                password=os.getenv("password"), host=os.getenv("host"),
                                port=os.getenv("port"))

        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()

        conn.close()
        return result

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        return self.__execute_query("SELECT name, amount FROM employers")


    def get_all_vacancies(self):
        """
        получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        """
        return self.__execute_query("SELECT employers.name, vacancies.name, salary_from, salary_to, url FROM vacancies INNER JOIN employers ON employers.id = vacancies.employer")