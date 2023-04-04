import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def check_user(tg_username):
    """ Check user in DB """
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
            cursor.execute("""SELECT COUNT(*) FROM users 
                              WHERE tg_username = %(tg_username)s """, {'tg_username': tg_username})
            alfa = cursor.fetchone()[0]
            print(f'[INFO] Number of users found = ', alfa)

            connection.commit()
            return alfa

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')
