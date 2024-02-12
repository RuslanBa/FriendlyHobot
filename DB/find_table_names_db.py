import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def find_table_names_db():
    """ Take table_names for finding messages for marking """
    try:
        # connect to exist database

        connection = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('MY_USER'),
            password=os.getenv('PASSWORD'),
            database=os.getenv('DB_NAME'),
            port=os.getenv('DB_PORT'),
            sslmode='require')

        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM channels")

            order_data = cursor.fetchall()
            result = []

            for row in order_data:
                table_name = row[1]
                result.append(table_name)

            connection.commit()
            return result

    except Exception as _ex:
        print('[INFO find_mes_for_marking_db] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO find_mes_for_marking_db] PostgreSQL connection close')

aaa = find_table_names_db()
print(aaa)
