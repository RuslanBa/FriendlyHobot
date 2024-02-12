import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def find_mes_for_marking_db(table_names):
    """ Take messages """

    sql = 'SELECT * FROM '

    for elements in table_names:
        sql = sql+str(elements)+' UNION ALL SELECT * FROM '

    end_sql = sql[:-25]
    print('[INFO] Full SQL for parsing - ', end_sql)

    try:
        connection = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('MY_USER'),
            password=os.getenv('PASSWORD'),
            database=os.getenv('DB_NAME'),
            port=os.getenv('DB_PORT'),
            sslmode='require')

        with connection.cursor() as cursor:

            cursor.execute(f"SELECT * FROM ({str(end_sql)}) AS mes "
                           f"WHERE check_admin = 'false' AND text_mes IS NOT NULL "
                           f"OR check_admin = 'false' AND text_mes != '' "
                           f"ORDER BY random() LIMIT 1")

            random_mes = cursor.fetchall()

            print(random_mes)

            connection.commit()
            return random_mes

    except Exception as _ex:
        print('[INFO find_mes_for_marking_db] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO find_mes_for_marking_db] PostgreSQL connection close')


# aaa = ['argentinabirth_1660919565', 'beautiarg_1785405798', 'argentinatrabajo_1708075997', 'ruargentinajob_1743123477']
# print(find_mes_for_marking_db(aaa))
