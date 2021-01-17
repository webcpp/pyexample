import pymysql.cursors
from pymysqlpool.pool import Pool
import json



def find(req,res,param):
    try:
        if req.has_form("id"):
            pool = Pool(host='127.0.0.1',port=3306, user='root', password='123456',database='testdb',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            pool.init()
            connection = pool.get_conn()
            cur = connection.cursor()
            cur.execute("SELECT * FROM `websites` WHERE `id`=%s;" , (int(req.get_form('id'))))
            result = cur.fetchone()
            pool.release(connection)
            res.header('Content-Type','application/json')
            res.content(json.dumps(result,ensure_ascii=False))
            res.status(200)
    except:
        res.content('Failed\n')
        res.status(500)

def handler(req,res,param):
    find(req,res,param)

