# import required package
import mysql.connector 
from mysql.connector import errorcode
from database_config import local_config

DB_NAME = 'AllWeatherQuant'
TABLES = {}
TABLES['assets'] = (
    "CREATE TABLE `assets` ("
    "  `Symbol` varchar(14) NOT NULL,"
    "  `ETF_Name` varchar(100) NOT NULL,"
    "  `Date` date NOT NULL,"
    "  `Asset_Classes` varchar(14) NOT NULL,"
    "  `Type` varchar(100),"
    "  `Currency` varchar(14),"
    "  `Duration` float(32,5),"
    "  `Open` float(32,5),"
    "  `High` float(32,5),"
    "  `Low` float(32,5),"
    "  `Close` float(32,5),"
    "  `Trading_Volume` float(32,5),"
    "  `Outstanding_Shares` float(32,5),"
    "  PRIMARY KEY `my_unique_key` (`Symbol`, `Date`)"
    ") ENGINE=InnoDB")

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

# connect to database(DB_NAME)
cnx = mysql.connector.connect(**local_config)
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