import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def delete_spec(id_user, spec_id):
    """ Delete 1 spec for user in DB """

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
            cursor.execute("""DELETE FROM user_spec WHERE id=%(spec_id)s and id_user=%(id_user)s """,
                           {'spec_id': spec_id, 'id_user': id_user})

            connection.commit()
            print(f'[INFO delete_spec] Spec for id_user {id_user} deleted with id - {spec_id}')

    except Exception as _ex:
        print('[INFO delete_spec] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO delete_spec] PostgreSQL connection close')
