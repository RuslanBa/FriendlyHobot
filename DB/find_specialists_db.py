import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def find_masters(spec_name):
    """ Take specialists """
    try:
        # connect to exist database

        connection = psycopg2.connect(
            host=os.getenv('HOST'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            database=os.getenv('DB_NAME'),
            port=os.getenv('DB_PORT'))

        with connection.cursor() as cursor:

            cursor.execute("""SELECT COUNT(*) FROM user_spec WHERE spec_name = %(spec_name)s::text""",
                           {'spec_name': spec_name})
            alfa = cursor.fetchone()[0]
            print('Number of specialists = ', alfa)

            if alfa > 0:
                cursor.execute("SELECT * FROM user_spec WHERE spec_name = %(spec_name)s::text",
                               {'spec_name': spec_name})

                user_data = cursor.fetchall()
                return user_data

                connection.commit()
                print(f'[INFO] Specialists found')
                # return tg_id, spec_about

            else:
                connection.commit()
                print(f'[INFO] Specialists not found')
                return 'n'

    except Exception as _ex:
        print('[INFO] find_masters. Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')
