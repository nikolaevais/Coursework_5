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