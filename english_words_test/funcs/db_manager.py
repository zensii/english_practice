import psycopg2
from psycopg2 import Error
from typing import Dict
from decouple import config
username = config('DB_USER')
password = config('DB_PASS')


class DatabaseManager:
    def __init__(self, user: str = username, passwd: str = password, dbname: str = "andy_words_dict", host: str = "192.168.1.249", port: str = "5432"):
        self.connection_params = {
            "dbname": dbname,
            "user": user,
            "password": passwd,
            "host": host,
            "port": port
        }
        self._ensure_table_exists()

    def _get_connection(self):
        return psycopg2.connect(**self.connection_params)

    def _ensure_table_exists(self) -> None:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS andy_words_dict (
            id SERIAL PRIMARY KEY,
            english_word VARCHAR(50) UNIQUE NOT NULL,
            bulgarian_word VARCHAR(50) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(create_table_query)
                    conn.commit()
        except Error as e:
            print(f"Error creating table: {e}")
            raise

    def add_word(self, english: str, bulgarian: str) -> None:
        insert_query = """
        INSERT INTO andy_words_dict (english_word, bulgarian_word)
        VALUES (%s, %s)
        ON CONFLICT (english_word) DO UPDATE 
        SET bulgarian_word = EXCLUDED.bulgarian_word;
        """
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(insert_query, (english, bulgarian))
                    conn.commit()
                    print(f"\nУспешно добави: {english} - {bulgarian} в речника.")
        except Error as e:
            print(f"Error adding word: {e}")
            raise

    def add_session(self, user: str, total_translations: int, total_errors: int, wrong_words: list) -> None:
        insert_query = """
        INSERT INTO sessions (player, translated_count, wrong_count, unknown_words)
        VALUES (%s, %s, %s, %s)
        """
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(insert_query, (user, total_translations, total_errors, ' '.join(wrong_words)))
                    conn.commit()
                    print(f"\nСесията е записана успешно.")
        except Error as e:
            print(f"Error adding word: {e}")
            raise


    def get_words_dict(self) -> Dict[str, str]:
        select_query = "SELECT english_word, bulgarian_word FROM andy_words_dict;"

        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(select_query)
                    results = cursor.fetchall()
                    words_dict = {row[0]: row[1] for row in results}
            return words_dict
        except Error as e:
            print(f"Error retrieving words: {e}")
            raise


if __name__ == '__main__':
    pass