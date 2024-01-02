import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def find_orders_db(id_user):
    """ Take orders """
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

            cursor.execute("SELECT * FROM orders WHERE id_user = %(id_user)s", {'id_user': id_user})

            order_data = cursor.fetchall()
            result = []

            for row in order_data:
                id_user = row[0]
                description = row[1]
                city = row[2]
                id_order = row[3]
                date = row[4]
                time = row[5]
                spec_name = row[6]
                uu = {'id_user': id_user, 'description': description, 'city': city, 'id_order': id_order,
                      'date': date, 'time': time, 'spec_name': spec_name}
                result.append(uu)

            connection.commit()
            return result

    except Exception as _ex:
        print('[INFO find_orders_db] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO find_orders_db] PostgreSQL connection close')
