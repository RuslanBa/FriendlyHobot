import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def find_speciality(id_spec):
    """ Take speciality from DB """
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

            cursor.execute("SELECT * FROM specialities WHERE id_spec = %(id_spec)s", {'id_spec': id_spec})

            spec_data = cursor.fetchone()
            name = spec_data[0]
            id_spec = spec_data[1]
            rus_name = spec_data[2]
            return name, id_spec, rus_name

            connection.commit()
            return name, about, city, username

    except Exception as _ex:
        print('[INFO find_speciality] find_people. Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO find_speciality] PostgreSQL connection close')
