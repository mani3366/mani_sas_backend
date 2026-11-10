from .db import get_db_connection


def test_database_connection():
    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT version();")
                result = cursor.fetchone()

                print("====================================")
                print("DATABASE CONNECTION SUCCESSFUL")
                print("====================================")
                print(result[0])

    except Exception as error:
        print("====================================")
        print("DATABASE CONNECTION FAILED")
        print("====================================")
        print(error)