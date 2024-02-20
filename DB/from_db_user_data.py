import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def user_data_by_id(id_user):
    """ Take user data from DB by id_user """
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
                           "WHERE id_user = %(id_user)s", {'id_user': id_user})

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
            country = user_data[11]
            phone = user_data[12]
            return name, tg_id, tg_name, tg_surname, tg_username, about, archetype, city, birthdate, \
                   speciality_need, country, phone

        connection.commit()
        print(f'[INFO user_data_by_id] Connection to users commit')

    except Exception as _ex:
        print('[INFO user_data_by_id] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO user_data_by_id] PostgreSQL connection close')


def user_spec(tg_username):
    """ Take user data from DB by tg_id """
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

            cursor.execute("SELECT * FROM user_spec WHERE tg_username = %(tg_username)s::text",
                           {'tg_username': tg_username})

            user_data = cursor.fetchall()
            result = []
            print(user_data)

            for row in user_data:
                id_user = row[0]
                spec_about = row[3]
                service_id = row[5]
                spec_id = row[7]

                cursor.execute(f"SELECT rus_name FROM specialities WHERE id_spec = '{spec_id}' ")
                spec_name = cursor.fetchall()
                spec_name = spec_name[0][0]

                uu = {'id_user': id_user, 'spec_name': spec_name, 'about': spec_about, 'service_id': service_id,
                      'spec_id': spec_id}
                result.append(uu)
            return result

        connection.commit()
        print(f'[INFO user_spec] Connection to user information commit')

    except Exception as _ex:
        print('[INFO user_spec] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO user_spec] PostgreSQL connection close')


# print(user_data_tg('176221727'))
#
# print(user_spec(176221727))
# us_spec = user_spec(176221727)
#
# for a in us_spec:
#     e = a['name']
#     f = a['about']
#     print(e, f)


# def xxxxxxxxx():
#     """ Take user data from DB by tg_id """
#     try:
#         # connect to exist database
#
#         connection = psycopg2.connect(
#             host=os.getenv('DB_HOST'),
#             user=os.getenv('MY_USER'),
#             password=os.getenv('PASSWORD'),
#             database=os.getenv('DB_NAME'),
#             port=os.getenv('DB_PORT'),
#             sslmode='require')
#
#         with connection.cursor() as cursor:
#
#             cursor.execute("SELECT * FROM user_spec WHERE spec_name is NOT NULL")
#             user_data = cursor.fetchall()
#
#             for elements in user_data:
#                 id_x = elements[6]
#                 spec_name = elements[1]
#                 print(f'id_x = {id_x}, spec_name = {spec_name}')
#
#                 cursor.execute(f"SELECT id_spec FROM specialities WHERE rus_name='{spec_name}' ")
#                 spec_id = cursor.fetchall()
#                 print(f'id_x = {id_x}, spec_name = {spec_name}, spec_id = {spec_id}')
#
#                 cursor.execute(f"UPDATE user_spec SET spec_id='{spec_id[0][0]}' WHERE id='{id_x}' ")
#
#         connection.commit()
#         print(f'[INFO user_spec] Connection to user information commit')
#
#     except Exception as _ex:
#         print('[INFO user_spec] Error while working with PostgreSQL', _ex)
#
#     finally:
#         if connection:
#             connection.close()
#             print('[INFO user_spec] PostgreSQL connection close')
