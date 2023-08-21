import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def change_fields(id_user, user_field, new_value):
    """ Add new abject in DB """
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
            if user_field == 'name':
                request = """UPDATE users SET name = %(new_value)s WHERE id_user = %(id_user)s"""
            elif user_field == 'country':
                request = """UPDATE users SET country = %(new_value)s WHERE id_user = %(id_user)s"""
            elif user_field == 'city':
                request = """UPDATE users SET city = %(new_value)s WHERE id_user = %(id_user)s"""
            elif user_field == 'about':
                request = """UPDATE users SET about = %(new_value)s WHERE id_user = %(id_user)s"""
            elif user_field == 'birthdate':
                request = """UPDATE users SET birthdate = %(new_value)s WHERE id_user = %(id_user)s"""
            elif user_field == 'phone':
                request = """UPDATE users SET phone = %(new_value)s WHERE id_user = %(id_user)s"""
            cursor.execute(request,
                           {'id_user': id_user, 'user_field': user_field, 'new_value': new_value})

        connection.commit()
        print(f'[INFO change_fields] Field changed. New value {new_value}')

    except Exception as _ex:
        print('[INFO change_fields] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO change_fields] PostgreSQL connection close')


# change_fields('176221727', 'name', 'rul')
