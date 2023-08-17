import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def find_people_by_city(city):
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

            cursor.execute("SELECT count(*) FROM user_spec WHERE spec_city = %(city)s", {'city': city})

            data = cursor.fetchone()
            quantity = data[0]
            print(quantity)
            return quantity

            connection.commit()
            return quantity

    except Exception as _ex:
        print('[INFO] find_people. Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')
