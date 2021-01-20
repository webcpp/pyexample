import pymysql
from dbutils.pooled_db import PooledDB

db_setting = {'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'password':'123456',
            'database':'testdb',
            'charset':'utf8mb4',
            'creator':pymysql,
            'autocommit':True,
            'blocking':False,
            'cursorclass':pymysql.cursors.DictCursor,
            'mincached':0,#the default of 0 means no connections are made at startup
            'maxcached':0,#the default value of 0 or None means unlimited pool size
            'maxconnections':0,#the default value of 0 or None means any number of connections)
            }


class dbhelp:
    def __init__(self,**config):
        self.__config = db_setting
        self.__config.update(config)
        self.__pool = PooledDB(**self.__config)
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
    def commit(self):
        self.__connection.commit()
    def rollback(self):
        self.__connection.rollback()
    def close(self):
        self.__cursor.close()
        self.__connection.close()
        



