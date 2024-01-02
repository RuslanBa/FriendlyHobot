import os
from dotenv import load_dotenv
import psycopg2
from datetime import datetime


load_dotenv()


def add_order(id_user, spec_name, description, city):
    """ Add new order in DB """
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

            date_added = datetime.now().date()
            time_added = datetime.now().time()
            time_added = time_added.strftime('%H:%M:%S')

            cursor.execute("INSERT INTO orders"
                           "(id_user, spec_name, description, city, date, time) "
                           "VALUES (%(id_user)s, %(spec_name)s, %(description)s, %(city)s, %(date)s, %(time)s) "
                           "RETURNING id_order",
                           {'id_user': id_user, 'spec_name': spec_name, 'description': description,
                            'city': city, 'date': date_added, 'time': time_added})

            new_order_id = cursor.fetchone()[0]

            connection.commit()
            print(f'[INFO add_order] Id for new connection user-speciality created - {new_order_id}')
            return new_order_id

    except Exception as _ex:
        print('[INFO add_spec] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO add_spec] PostgreSQL connection close')

