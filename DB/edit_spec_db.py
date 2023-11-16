import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()


def edit_spec(id_user, spec_id, new_text):
    """ Edit 1 spec for user in DB """

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
            print(f'[INFO edit_spec] Try to change spec_about of id {spec_id} for id_user {id_user}')
            cursor.execute("""UPDATE user_spec 
                              SET spec_about=%(new_text)s 
                              WHERE id=%(spec_id)s and id_user=%(id_user)s """,
                           {'new_text': new_text, 'spec_id': spec_id, 'id_user': id_user})

            connection.commit()
            print(f'[INFO edit_spec] Spec for id_user {id_user} changed with id - {spec_id}')

    except Exception as _ex:
        print('[INFO edit_spec] Error while working with PostgreSQL', _ex)

    finally:
        if connection:
            connection.close()
            print('[INFO edit_spec] PostgreSQL connection close')
