import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def statistic_mes(table_names):
    """ Take quantities of messages id DB """

    sql = 'SELECT * FROM '
    for elements in table_names:
        sql = sql+str(elements)+' UNION ALL SELECT * FROM '
    end_sql = sql[:-25]

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

            cursor.execute(f"SELECT count(*) FROM ({str(end_sql)}) AS mes ")
            count_all = cursor.fetchall()
            count_all = count_all[0][0]

            cursor.execute(f"SELECT count(*) FROM ({str(end_sql)}) AS mes "
                           f"WHERE check_admin = 'True' ")
            count_check_admin = cursor.fetchall()
            count_check_admin = count_check_admin[0][0]

            cursor.execute(f"SELECT count(*) FROM ({str(end_sql)}) AS mes "
                           f"WHERE intent IS NOT NULL AND intent != 'none_target' ")
            count_intents = cursor.fetchall()
            count_intents = count_intents[0][0]

            stat_specs = []
            cursor.execute("SELECT * FROM specialities")
            data_specialities = cursor.fetchall()

            for elements in data_specialities:
                id_spec = elements[1]
                spec_name = elements[2]

                cursor.execute(f"SELECT count(*) FROM ({str(end_sql)}) AS mes "
                               f"WHERE spec_id = '{elements[1]}' AND intent = 'suggest_service' ")
                num = cursor.fetchall()
                suggest = num[0][0]

                cursor.execute(f"SELECT count(*) FROM ({str(end_sql)}) AS mes "
                               f"WHERE spec_id = '{elements[1]}' AND intent = 'need_specialist' ")
                num = cursor.fetchall()
                wanted = num[0][0]

                stat_speciality = {'id_spec': id_spec, 'услуга': spec_name, 'предлагают': suggest, 'ищут': wanted}
                print(stat_speciality)

                stat_specs.append(stat_speciality)

            connection.commit()
            return count_all, count_check_admin, count_intents, stat_specs

    except Exception as _ex:
        print('[INFO find_mes_for_marking_db] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO find_mes_for_marking_db] PostgreSQL connection close')


# def iiiiiiiiii():
#     """ Take quantities of messages id DB """
#
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
#             cursor.execute(f"SELECT * FROM argentinabirth_1660919565 "
#                            f"WHERE intent is NOT NULL AND intent != 'none_target' "
#                            f"AND intent NOT IN ('need_sell', 'need_buy') ")
#             user_data = cursor.fetchall()
#             print(user_data)
#
#             for elements in user_data:
#                 print(elements)
#                 mes_id = elements[0]
#                 intent = elements[8]
#                 data = intent.split('_')
#                 intent = str(data[0])+'_'+str(data[1])
#                 spec_name = str(data[2])
#                 print(spec_name)
#
#                 # cursor.execute(f"SELECT id_spec FROM specialities WHERE rus_name='{spec_name}' ")
#                 # spec_id = cursor.fetchall()
#                 # spec_id = spec_id[0][0]
#                 #
#                 # print(f'mes_id = {mes_id}, intent = {intent}, spec_name = {spec_name}, spec_id = {spec_id}')
#
#                 cursor.execute(f"UPDATE argentinabirth_1660919565 SET intent='{intent}' "
#                                f"WHERE message_id='{mes_id}' ")
#                 print('готово)')
#
#             connection.commit()
#
#     except Exception as _ex:
#         print('[INFO find_mes_for_marking_db] Error while working with PostgreSQL', _ex)
#
#     finally:
#         if connection:
#             connection.close()
#             print('[INFO find_mes_for_marking_db] PostgreSQL connection close')


# aaa = ['argentinabirth_1660919565', 'beautiarg_1785405798', 'argentinatrabajo_1708075997', 'ruargentinajob_1743123477']
# print(statistic_mes(aaa))
