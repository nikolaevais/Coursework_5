import psycopg2
import dotenv
import os
from src.api_hh import HHApi

dotenv.load_dotenv()

def create_database(db_name):
    """подключение, удаление базы данных при её наличии, и создание новой базы данных"""
    conn = psycopg2.connect(dbname="postgres", user=os.getenv("user"),
                            password=os.getenv("password"), host=os.getenv("host"),
                            port=os.getenv("port"))

    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cur.execute(f"CREATE DATABASE {db_name}")

    cur.close()
    conn.close()



def create_tables(db_name):
    """подключение к базе данных и создание в ней двух таблиц: employers, vacancies"""
    conn = psycopg2.connect(dbname=db_name, user=os.getenv("user"),
                            password=os.getenv("password"), host=os.getenv("host"),
                            port=os.getenv("port"))

    with conn:
        with conn.cursor() as cur:
            cur.execute("""CREATE TABLE employers (
                        id INTEGER PRIMARY KEY,
                        name VARCHAR(100) UNIQUE NOT NULL,
                        amount INTEGER NOT NULL
                        )
                        """)

            cur.execute("""CREATE TABLE vacancies (
                        id INTEGER PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        url VARCHAR(100) NOT NULL,
                        salary_from INTEGER,
                        salary_to INTEGER,
                        employer INTEGER REFERENCES employers(id),
                        area VARCHAR(100) NOT NULL
                        )
                        """)

    conn.close()


def insert_data_in_tables(db_name):
    """заполнение данными таблиц employers, vacancies"""
    hh = HHApi()
    employers = hh.get_employers()
    vacancies = hh.get_all_vacancies()
    conn = psycopg2.connect(dbname=db_name, user=os.getenv("user"),
                                password=os.getenv("password"), host=os.getenv("host"),
                                port=os.getenv("port"))
    with conn:
        with conn.cursor() as cur:
            for employer in employers:
                    cur.execute("""INSERT INTO employers VALUES (%s, %s, %s)""", (employer["id"], employer ["name"], employer["amount"]))
            for vacancy in vacancies:
                    cur.execute("""INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s)""", (vacancy["id"], vacancy["name"], vacancy["url"],
                                                                                              vacancy["salary_from"], vacancy["salary_to"], vacancy["employer"], vacancy["area"]))
    conn.close()