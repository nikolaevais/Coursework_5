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