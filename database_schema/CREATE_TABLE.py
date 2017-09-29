import mysql.connector 
from mysql.connector import errorcode

def Create_Table(DB_NAME, config, TABLES):
    # connect to database(DB_NAME)
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    try:
        cursor.database = DB_NAME
    except mysql.connector.Error as err:
        print(err)
        exit(1)

    # create table with schema
    for name, ddl in TABLES.items():
        try:
            print("Creating table {}: ".format(name), end='')
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.close()