import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def find_people(id_user):
    """ Take specialists """
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

            cursor.execute("SELECT * FROM users WHERE id_user = %(id_user)s", {'id_user': id_user})

            user_data = cursor.fetchone()
            name = user_data[0]
            tg_id = user_data[1]
            tg_name = user_data[2]
            tg_surname = user_data[3]
            tg_username = user_data[4]
            about = user_data[5]
            archetype = user_data[6]
            city = user_data[7]
            birthdate = user_data[8]
            speciality_need = user_data[9]
            country = user_data[11]
            return name, tg_id, tg_name, tg_surname, tg_username, about, archetype, city, birthdate, \
                   speciality_need, country

            connection.commit()
            return name, about, city, username

    except Exception as _ex:
        print('[INFO] find_people. Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')
