import os
from dotenv import load_dotenv
import psycopg2
from datetime import datetime


load_dotenv()


def add_new_log(tg_id, tg_username, activity):
    """ Add new log in DB """
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("MY_USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT"),
            sslmode="require")

        with connection.cursor() as cursor:

            date_added = datetime.now().date()
            time_added = datetime.now().time()
            time_added = time_added.strftime('%H:%M:%S')

            cursor.execute("INSERT INTO logs"
                           "(tg_id, tg_username, activity, date, time) "
                           "VALUES (%(tg_id)s, %(tg_username)s, %(activity)s, %(date)s, %(time)s) ",
                           {'tg_id': tg_id, 'tg_username': tg_username, 'activity': activity, 'date': date_added,
                            'time': time_added})

        connection.commit()
        print(f'[INFO] New log created')

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
