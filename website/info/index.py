import pymysql
import pymysql.cursors
from dbutils.persistent_db import PersistentDB
import json


def find(req,res,param):
    try:
        if req.has_form("id"):
            pool = PersistentDB(pymysql,host='127.0.0.1',port=3306, user='root', password='123456',database='testdb',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            connection = pool.connection()
            cur = connection.cursor()
            cur.execute("SELECT * FROM `websites` WHERE `id`=%s;" , (int(req.get_form('id'))))
            result = cur.fetchone()
            cur.close()
            connection.close()
            res.header('Content-Type','application/json')
            res.content(json.dumps(result,ensure_ascii=False))
            res.status(200)
    except:
        res.content('Failed\n')
        res.status(500)

def handler(req,res,param):
    find(req,res,param)

