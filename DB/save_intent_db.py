import os
from dotenv import load_dotenv
import psycopg2
from datetime import datetime


load_dotenv()


def save_intent_db(table_name, message_id, intent, spec_id):
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("MY_USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT"),
            sslmode="require")

        with connection.cursor() as cursor:

            cursor.execute(f"""UPDATE {table_name} SET intent = %(intent)s, check_admin = '1', 
                              spec_id = %(spec_id)s WHERE message_id = %(message_id)s """,
                           {'intent': intent, 'spec_id': spec_id, 'message_id': message_id})

            connection.commit()
            print(f'[INFO save_intent_db] '
                  f'In {table_name} for message with message_id {message_id} set new intent {intent} '
                  f'and spec_id = {spec_id}')

    except Exception as _ex:
        print('[INFO save_intent_db] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO save_intent_db] PostgreSQL connection close')
