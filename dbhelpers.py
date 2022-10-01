import mariadb
import dbcreds

def connect_db():
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        return cursor
    except mariadb.DatabaseError as error:
        print('DATABASE ERROR', error)
        return str(error)
    except mariadb.DataError as error:
        print('DATA ERROR', error)
        return str(error)
    except mariadb.PoolError as error:
        print('POOL ERROR', error)
        return str(error)
    except mariadb.InternalError as error:
        print('INTERNAL ERROR', error)
        return str(error)
    except mariadb.IntegrityError as error:
        print('INTEGRITY ERROR', error)
        return str(error)
    except mariadb.InterfaceError as error:
        print('INTERFACE ERROR', error)
        return str(error)
    except mariadb.OperationalError as error:
        print('OPERATIONAL ERROR', error)
        return str(error)
    except mariadb.ProgrammingError as error:
        print('PROGRAMMING ERROR', error)
        return str(error)
    except mariadb.NotSupportedError as error:
        print('NOT SUPPORTED ERROR', error)
        return str(error)
    except mariadb.Warning as error:
        print('WARNING', error)
        return str(error)
    except Exception as error:
        print('UNKNOWN ERROR', error)
        return str(error)
    except mariadb.TypeError as error:
        print('TYPE ERROR', error)
        return str(error)
    except mariadb.Error as error:
        print('ERROR', error)
        return str(error)
   
def execute_statement(cursor, statement, list=[]):
    try:
        cursor.execute(statement, list)
        result = cursor.fetchall()
        return result
    except mariadb.DatabaseError as error:
        print('DATABASE ERROR', error)
        return str(error)
    except mariadb.DataError as error:
        print('DATA ERROR', error)
        return str(error)
    except mariadb.PoolError as error:
        print('POOL ERROR', error)
        return str(error)
    except mariadb.InternalError as error:
        print('INTERNAL ERROR', error)
        return str(error)
    except mariadb.IntegrityError as error:
        print('INTEGRITY ERROR', error)
        return str(error)
    except mariadb.InterfaceError as error:
        print('INTERFACE ERROR', error)
        return str(error)
    except mariadb.OperationalError as error:
        print('OPERATIONAL ERROR', error)
        return str(error)
    except mariadb.ProgrammingError as error:
        print('PROGRAMMING ERROR', error)
        return str(error)
    except mariadb.NotSupportedError as error:
        print('NOT SUPPORTED ERROR', error)
        return str(error)
    except mariadb.Warning as error:
        print('WARNING', error)
        return str(error)
    except Exception as error:
        print('UNKNOWN ERROR', error)
        return str(error)
    except mariadb.TypeError as error:
        print('TYPE ERROR', error)
        return str(error)
    except mariadb.Error as error:
        print('ERROR', error)
        return str(error)
def close_connection(cursor):
    try:
        conn = cursor.connection
        cursor.close()
        conn.close()
    except mariadb.DatabaseError as error:
        print('DATABASE ERROR', error)
        return str(error)
    except mariadb.DataError as error:
        print('DATA ERROR', error)
        return str(error)
    except mariadb.PoolError as error:
        print('POOL ERROR', error)
        return str(error)
    except mariadb.InternalError as error:
        print('INTERNAL ERROR', error)
        return str(error)
    except mariadb.IntegrityError as error:
        print('INTEGRITY ERROR', error)
        return str(error)
    except mariadb.InterfaceError as error:
        print('INTERFACE ERROR', error)
        return str(error)
    except mariadb.OperationalError as error:
        print('OPERATIONAL ERROR', error)
        return str(error)
    except mariadb.ProgrammingError as error:
        print('PROGRAMMING ERROR', error)
        return str(error)
    except mariadb.NotSupportedError as error:
        print('NOT SUPPORTED ERROR', error)
        return str(error)
    except mariadb.Warning as error:
        print('WARNING', error)
        return str(error)
    except Exception as error:
        print('UNKNOWN ERROR', error)
        return str(error)
    except mariadb.TypeError as error:
        print('TYPE ERROR', error)
        return str(error)
    except mariadb.Error as error:
        print('ERROR', error)
        return str(error)

def conn_exe_close(statement,list):
    cursor = connect_db()
    if(cursor == None):
        return 'connection error'
    result = execute_statement(cursor, statement, list)
    if(result == None):
        return 'statement error'
    close_connection(cursor)
    return result