import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def delete_order_db(id_user, id_order):
    """ Delete 1 order for user in DB """

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

            print(f'[INFO delete_order_db] Trying to delete order - {id_order} for user - {id_user}')

            cursor.execute("""DELETE FROM orders WHERE id_order=%(id_order)s and id_user=%(id_user)s """,
                           {'id_order': id_order, 'id_user': id_user})

            connection.commit()
            print(f'[INFO delete_order_db] Order for id_user {id_user} deleted with id - {id_order}')

    except Exception as _ex:
        print('[INFO delete_order_db] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO delete_order_db] PostgreSQL connection close')
