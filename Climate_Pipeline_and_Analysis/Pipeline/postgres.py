'''
POSTGRES
'''

import psycopg2

uid = "postgres"
pwd = "password"
host = "127.0.0.1"
port = "5433"
database = "postgres"

# TODO: Load


def test():
    try:
        conn = psycopg2.connect(database=database, user=uid, password=pwd, host=host, port=port)

        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS TEST")

        test_sql_create = '''
        CREATE TABLE TEST(
            FIRST_NAME CHAR(20) NOT NULL,
            LAST_NAME CHAR(20)
        )
        '''
        cursor.execute(test_sql_create)

        test_sql_insert = "INSERT INTO TEST(FIRST_NAME, LAST_NAME) VALUES ('Mitchell','Joram')"
        cursor.execute(test_sql_insert)

        test_sql_select = "SELECT * from TEST"
        cursor.execute(test_sql_select)
        result = cursor.fetchall()
        print(result)

        test_sql_update = "UPDATE TEST SET FIRST_NAME = 'John' WHERE FIRST_NAME = 'Mitchell'"
        cursor.execute(test_sql_update)

        cursor.execute(test_sql_select)
        result = cursor.fetchall()
        print(result)

        conn.commit()

        conn.close()
    except Exception as e:
        print("Postgres error: " + str(e))


try: 
    test()
except Exception as e:
    print("Test error: " + str(e))