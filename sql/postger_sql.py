import psycopg2 as sq
from config import host, db_name, user, password

async def sql_start():
    try:
        #connect
        conection = sq.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
        )
        
        table = '''CREATE TABLE IF NOT EXISTS records (
    id        SERIAL  PRIMARY KEY,
    user_id   INTEGER  NOT NULL,
    date      TIMESTAMP NOT NULL DEFAULT(CURRENT_TIMESTAMP),
    operation BOOLEAN  NOT NULL,
    value     INTEGER  NOT NULL
);'''
        
        conection.autocommit = True
        
        curs = conection.cursor()
        curs.execute(table)
        
        print('База данных подключена')
    
    except sq.Error as e:
        print('Error', e)
    
    finally:
        curs.close()
        conection.close()

async def sql_earn(user_id , value):

    operation = True
    user_id = int(user_id)
    
    try:
        #connect
        conection = sq.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
        )

        conection.autocommit = True

        curs = conection.cursor()

        curs.execute('INSERT INTO records(user_id, operation, value) VALUES(%s, %s, %s)',[user_id, operation, value])
        conection.commit()
    
    except sq.Error as e:
        print('Error',e)
    
    finally:
        curs.close()
        conection.close()

async def sql_expens(user_id , value):
    operation = False
    user_id = int(user_id)
    
    try:
        #connect
        conection = sq.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
        )

        conection.autocommit = True

        curs = conection.cursor()

        curs.execute('INSERT INTO records(user_id, operation, value) VALUES(%s, %s, %s)',[user_id, operation, value])
        conection.commit()
    
    except sq.Error as e:
        print('Error',e)
    
    finally:
        curs.close()
        conection.close()

def opinion_sql(user_id):
    try:
        #connect
        conection = sq.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
        )

        conection.autocommit = True

        curs = conection.cursor()

        curs.execute('SELECT * FROM records WHERE user_id = %s', [user_id])

        message = curs.fetchall()
        
        return message

    except sq.Error as e:
        print('Error',e)
    
    finally:
        curs.close()
        conection.close()