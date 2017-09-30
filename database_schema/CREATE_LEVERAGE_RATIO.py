# import required package
from database_config import local_config
from CREATE_TABLE import Create_Table

DB_NAME = 'AllWeatherQuant'
TABLES = {}
TABLES['Leverage_ratio'] = (
    "CREATE TABLE `Leverage_ratio` ("
    "  `Symbol` varchar(14) NOT NULL,"
    "  `Date` date NOT NULL,"
    "  `Frequency_Day` int(8),"
    "  `Num_Days` int(8),"
    "  `Risk` float(32,5),"
    "  `Leverage_ratio` float(32,5),"
    "  PRIMARY KEY `my_unique_key` (`Symbol`, `Date`, `Frequency_Day`, `Num_Days`)"
    ") ENGINE=InnoDB")

Create_Table('AllWeatherQuant', local_config, TABLES)
