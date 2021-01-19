import pymysql
import pymysql.cursors
from dbutils.pooled_db import PooledDB

def get_config():
    return {'host':'127.0.0.1',
    'port':3306,
    'username':'root',
    'password':'123456',
    'database':'testdb',
    'charset':'utf8mb4'}

class dbhelp:
    def __init__(self):
        self.__config = get_config()
        self.__pool = PooledDB(pymysql,
                        cursorclass=pymysql.cursors.DictCursor,
                        host=self.__config['host'],
                        port=self.__config['port'],
                        user=self.__config['username'],
                        password=self.__config['password'],
                        database=self.__config['database'],
                        charset=self.__config['charset'])
        self.__connection = self.__pool.connection()
        self.__cursor = self.__connection.cursor()
    def execute(self,sql,*argv):
        return self.__cursor.execute(sql,*argv)
    def fetchone(self):
        return self.__cursor.fetchone()
    def fetchall(self):
        return self.__cursor.fetchall()
    def fetchmany(self,number_of_records):
        return self.__cursor.fetchmany(number_of_records)
    def close(self):
        self.__cursor.close()
        self.__connection.close()
        



