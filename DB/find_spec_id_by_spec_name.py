import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def find_spec_id(spec_name):
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

            cursor.execute(f"SELECT id_spec FROM specialities WHERE rus_name = '{spec_name}' ")

            spec_data = cursor.fetchone()
            spec_id = spec_data[0]
            return spec_id

            connection.commit()
            return name, about, city, username

    except Exception as _ex:
        print('[INFO find_speciality] find_people. Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO find_speciality] PostgreSQL connection close')


# aaa = find_spec_id('Языки')
# print(aaa)
