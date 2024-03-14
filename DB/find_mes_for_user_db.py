import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def find_mes_for_user_db(first_intent, spec_id):
    """ Take messages """

    try:
        connection = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('MY_USER'),
            password=os.getenv('PASSWORD'),
            database=os.getenv('DB_NAME'),
            port=os.getenv('DB_PORT'),
            sslmode='require')

        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM channels")
            order_data = cursor.fetchall()
            result = []
            for row in order_data:
                table_name = row[1]
                result.append(table_name)

            sql = 'SELECT * FROM '
            for elements in result:
                sql = sql + str(elements) + ' UNION ALL SELECT * FROM '
            end_sql = sql[:-25]
            print('[INFO find_mes_for_user_db] Full SQL for parsing - ', end_sql)

            print(f'[NFO find_mes_for_user_db] Trying to find mes for spec_id = "{spec_id}" '
                  f'and intent = "{first_intent}"')

            cursor.execute(f"SELECT * FROM ({str(end_sql)}) AS mes "
                           f"WHERE spec_id = '{spec_id}' AND intent = '{first_intent}' ")

            result_mes = cursor.fetchall()
            print('result mes = ', result_mes)

            connection.commit()
            return result_mes

    except Exception as _ex:
        print('[INFO find_mes_for_user_db] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO find_mes_for_user_db] PostgreSQL connection close')


# aaa = ['argentinabirth_1660919565', 'beautiarg_1785405798', 'argentinatrabajo_1708075997', 'ruargentinajob_1743123477']
# print(find_mes_for_marking_db(aaa))
