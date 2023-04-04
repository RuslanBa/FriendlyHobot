import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def user_data_tg(tg_username):
    """ Take user data from DB by tg_username """
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
                           "WHERE tg_username = %(tg_username)s::text", {'tg_username': tg_username})

            user_data = cursor.fetchone()
            name = user_data[0]
            about = user_data[5]
            city = user_data[8]
            birthdate = user_data[9]
            return name, about, city, birthdate

        connection.commit()
        print(f'[INFO] Connection to users commit')

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')


def user_spec(tg_username):
    """ Take user data from DB by tg_id """
    try:
        # connect to exist database

        connection = psycopg2.connect(
            host=os.getenv('HOST'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            database=os.getenv('DB_NAME'),
            port=5432)

        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM user_spec WHERE tg_username = %(tg_username)s::text",
                           {'tg_username': tg_username})

            user_data = cursor.fetchall()
            result = []

            for row in user_data:
                spec_name = row[1]
                spec_about = row[4]
                uu = {'name': spec_name, 'about': spec_about}
                result.append(uu)
            return result

        connection.commit()
        print(f'[INFO] Connection to user information commit')

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')


# print(user_data_tg('176221727'))
#
# print(user_spec(176221727))
# us_spec = user_spec(176221727)
#
# for a in us_spec:
#     e = a['name']
#     f = a['about']
#     print(e, f)
