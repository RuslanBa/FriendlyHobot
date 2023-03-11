import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def find_people(id_user):
    """ Take specialists """
    try:
        # connect to exist database

        connection = psycopg2.connect(
            host=os.getenv('HOST'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            database=os.getenv('DB_NAME'),
            port=os.getenv('DB_PORT'))

        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM users WHERE id_user = %(id_user)s", {'id_user': id_user})

            user_data = cursor.fetchone()
            print(user_data)
            name = user_data[0]
            username = user_data[4]
            about = user_data[5]
            city = user_data[8]

            connection.commit()
            return name, about, city, username

    except Exception as _ex:
        print('[INFO] find_people. Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')
