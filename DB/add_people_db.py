import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def add_new_people(name, tg_id, tg_name, tg_surname, tg_username, city):
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
            cursor.execute("INSERT INTO users"
                           "(name, tg_id, tg_name, tg_surname, tg_username, city) "
                           "VALUES (%(name)s, %(tg_id)s, %(tg_name)s, %(tg_surname)s, %(tg_username)s, "
                           "%(city)s) "
                           "RETURNING id_user",
                           {'name': name, 'tg_id': tg_id, 'tg_name': tg_name, 'tg_surname': tg_surname,
                            'tg_username': tg_username, 'city': city})

            id_of_new_row = cursor.fetchone()[0]
            print(id_of_new_row)

        connection.commit()
        print(f'[INFO] New user created - id - {id_of_new_row}')
        return id_of_new_row

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')


# Create new column with serial id ----------------------------------------------------------

# with connection.cursor() as cursor:
#     cursor.execute(
#         """ALTER TABLE objects
#         ADD Id SERIAL NOT NULL"""
#     )
#     connection.commit()
#     print('готово')
