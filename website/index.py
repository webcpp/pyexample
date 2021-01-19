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
        self.config = get_config()
        self.pool = PooledDB(pymysql,
        cursorclass=pymysql.cursors.DictCursor,
        host=self.config['host'],
        port=self.config['port'],
        user=self.config['username'],
        password=self.config['password'],
        database=self.config['database'],
        charset=self.config['charset'])
        self.connection = self.pool.connection()
        self.cursor = self.connection.cursor()
    def execute(self,sql,*argv):
        return self.cursor.execute(sql,*argv)
    def fetchone(self):
        return self.cursor.fetchone()
    def fetchall(self):
        return self.cursor.fetchall()
    def fetchmany(self,number_of_records):
        return self.cursor.fetchmany(number_of_records)
    def close(self):
        self.cursor.close()
        self.connection.close()
        



