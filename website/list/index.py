import pymysql.cursors
from pymysqlpool.pool import Pool
import json



def findall(req,res,param):
    try:
        pool = Pool(host='127.0.0.1',port=3306, user='root', password='123456',database='testdb',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        pool.init()
        connection = pool.get_conn()
        cur = connection.cursor()
        order = 'DESC'
        start = 0
        size = 5
        if req.has_form('order'):
            order = req.get_form('order')
        if(req.has_form('start')):
            start = int(req.get_form('start'))
        if(req.has_form('size')):
            size = int(req.get_form('size'))
        cur.execute("SELECT * FROM `websites` ORDER BY `id` {} LIMIT %s,%s;".format(order),(start,size))
        result = cur.fetchall()
        pool.release(connection)
        res.header('Content-Type','application/json')
        res.content(json.dumps(result,ensure_ascii=False))
        res.status(200)
    except:
        res.content('Failed\n')
        res.status(500)

def handler(req,res,param):
    findall(req,res,param)

