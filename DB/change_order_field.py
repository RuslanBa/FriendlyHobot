import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def change_fields_ord(id_order, order_field, new_value):
    """ Change order in DB """
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
            if order_field == 'description':
                request = """UPDATE orders SET description = %(new_value)s WHERE id_order = %(id_order)s"""
            elif order_field == 'city':
                request = """UPDATE orders SET city = %(new_value)s WHERE id_order = %(id_order)s"""
            elif order_field == 'spec_id':
                request = """UPDATE orders SET spec_id = %(new_value)s WHERE id_order = %(id_order)s"""

            cursor.execute(request,
                           {'id_order': id_order, 'order_field': order_field, 'new_value': new_value})

        connection.commit()
        print(f'[INFO change_fields_ord] Field changed. New value {new_value}')

    except Exception as _ex:
        print('[INFO change_fields_ord] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO change_fields_ord] PostgreSQL connection close')


# change_fields_ord('3', 'city', '22323')
