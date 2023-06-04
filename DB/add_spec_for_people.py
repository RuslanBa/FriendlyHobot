import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def add_spec(id_user, spec_name, spec_about, spec_city, tg_username):
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
            cursor.execute("""SELECT COUNT(*) FROM user_spec 
                              WHERE tg_username = %(tg_username)s and spec_name = %(spec_name)s """,
                           {'tg_username': tg_username, 'spec_name': spec_name})
            alfa = cursor.fetchone()[0]
            print('У пользователя уже есть такая специальнось, строк = ', alfa)

            if alfa > 0:
                cursor.execute("""UPDATE user_spec SET spec_about = %(spec_about)s WHERE tg_username = %(tg_username)s 
                               AND spec_name = %(spec_name)s AND spec_city = %(spec_city)s """,
                               {'spec_about': spec_about, 'tg_username': tg_username, 'spec_name': spec_name,
                                'spec_city': spec_city})
                connection.commit()
                print(f'[INFO] Connection user-speciality updated')

            else:
                cursor.execute("INSERT INTO user_spec"
                               "(id_user, spec_name, spec_about, spec_city, tg_username) "
                               "VALUES (%(id_user)s, %(spec_name)s, %(spec_about)s, %(spec_city)s, %(tg_username)s) "
                               "RETURNING id",
                               {'id_user': id_user, 'spec_name': spec_name, 'spec_about': spec_about,
                                'spec_city': spec_city, 'tg_username': tg_username})

                id_of_new_row = cursor.fetchone()[0]
                print(id_of_new_row)

                connection.commit()
                print(f'[INFO] Id for new connection user-speciality created - {id_of_new_row}')
                return id_of_new_row

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')
