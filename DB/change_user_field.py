import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def change_fields(tg_username, user_field, new_value):
    """ Add new abject in DB """
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            database=os.getenv('DB_NAME'),
            port=os.getenv('DB_PORT'),
            sslmode='require')

        with connection.cursor() as cursor:
            if user_field == 'name':
                request = """UPDATE users SET name = %(new_value)s WHERE tg_username = %(tg_username)s"""
            elif user_field == 'city':
                request = """UPDATE users SET city = %(new_value)s WHERE tg_username = %(tg_username)s"""
            elif user_field == 'about':
                request = """UPDATE users SET about = %(new_value)s WHERE tg_username = %(tg_username)s"""
            elif user_field == 'birthdate':
                request = """UPDATE users SET birthdate = %(new_value)s WHERE tg_username = %(tg_username)s"""
            cursor.execute(request,
                           {'tg_username': tg_username, 'user_field': user_field, 'new_value': new_value})

        connection.commit()
        print(f'[INFO] Field changed. New value {new_value}')

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')


# change_fields('176221727', 'name', 'rul')
