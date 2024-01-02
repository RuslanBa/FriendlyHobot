import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def check_user_tgid(tg_id):
    """ Check user in DB """
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
            cursor.execute("SELECT * FROM users "
                           "WHERE tg_id = %(tg_id)s", {'tg_id': str(tg_id)})

            user_data = cursor.fetchone()
            print(user_data)
            name = user_data[0]
            tg_id = user_data[1]
            tg_name = user_data[2]
            tg_surname = user_data[3]
            tg_username = user_data[4]
            about = user_data[5]
            archetype = user_data[6]
            city = user_data[7]
            birthdate = user_data[8]
            speciality_need = user_data[9]
            id_user = user_data[10]
            country = user_data[11]
            phone = user_data[12]
            return name, tg_id, tg_name, tg_surname, tg_username, about, archetype, city, birthdate, \
                   speciality_need, id_user, country, phone

    except Exception as _ex:
        print('[INFO check_user_tgid] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO check_user_tgid] PostgreSQL connection close')


# check_user_tgid('126206446')
