import psycopg2
from psycopg2 import sql

from typing import List, Tuple
from collections import namedtuple

def _connect() -> psycopg2.extensions.connection:
    connection_string = "postgres://ego:FQJZpN20uMnw4xhRPysEw7IMhhdMQEtC@dpg-cmv6sl0l5elc73ecn7ug-a.frankfurt-postgres.render.com/feddingcom"
    return psycopg2.connect(connection_string)

def create_table():
    with _connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS test (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255),
                    value VARCHAR(255)
                )
            """)
            conn.commit()

def query_all_rows() -> List[dict]:
    with _connect() as conn:
        query = sql.SQL("SELECT * FROM test")
        with conn.cursor() as cursor:
            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]
            Row = namedtuple('Row', columns)
            return [Row(*row)._asdict() for row in cursor.fetchall()]

def main():
    create_table()
    result = query_all_rows()
    print(result)

main()