import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def find_user_id(tg_username):
    """ Take user data from DB by tg_username """
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

            cursor.execute("""SELECT * FROM users WHERE tg_username = %(tg_username)s""",
                           {'tg_username': tg_username})

            id_user = cursor.fetchone()[10]
            print('Найден пользователь с id_user - ', id_user)
            return id_user

        connection.commit()
        print(f'[INFO] Connection to users commit')

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')
