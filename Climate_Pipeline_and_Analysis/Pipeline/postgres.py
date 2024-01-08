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
def load(data):
    try:
        print("Loading data into Postgres...")
        
        conn = psycopg2.connect(database=database, user=uid, password=pwd, host=host, port=port)
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS CLIMATE")

        sql_create = '''
        CREATE TABLE CLIMATE(
            STATE_ABBR CHAR(2) NOT NULL,
            YEAR INT,
            ACTIVITY VARCHAR(50),
            ACTIVITY_VALUE DECIMAL,
            ACTIVITY_UNIT VARCHAR(4),
            CO2_EQUIVALENT DECIMAL,
            CO2_EQUIVALENT_UNIT VARCHAR(4)
        )
        '''
        cursor.execute(sql_create)

        for state in data:
            sql_insert = f'''INSERT INTO CLIMATE VALUES (
                    '{state['state']}',
                    {state['year']},
                    '{state['activity']}',
                    {state['activity_value']},
                    '{state['activity_unit']}',
                    {state['co2e']},
                    '{state['co2e_unit']}'
                )
                '''
            cursor.execute(sql_insert)
        
        sql_select = "SELECT * FROM CLIMATE"
        cursor.execute(sql_select)
        result = cursor.fetchall()
        print("LOADED: " + str(result))

        conn.commit()

        conn.close()
        print("Finished loading data into Postgres.")
    except Exception as e:
        print("Load error: " + str(e))



# Test Postgres
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


# try: 
#     print("Executing Postgres test...")
#     test()
#     print("Finished Postgres test...")
# except Exception as e:
#     print("Test error: " + str(e))