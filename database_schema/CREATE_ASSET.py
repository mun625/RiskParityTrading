# import required package
from database_config import local_config
from CREATE_TABLE import Create_Table

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

Create_Table('AllWeatherQuant', local_config, TABLES)
