import pymysql
import pymysql.cursors
from dbutils.pooled_db import PooledDB
import json
from website.index import get_config


def findall(req,res,param):
    try:
        config = get_config()
        pool = PooledDB(pymysql,cursorclass=pymysql.cursors.DictCursor,host=config['host'],port=config['port'], user=config['username'], password=config['password'],database=config['database'],charset=config['charset'])
        connection = pool.connection()
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
        cur.close()
        connection.close()
        res.header('Content-Type','application/json')
        res.content(json.dumps(result,ensure_ascii=False))
        res.status(200)
    except Exception as e:
        res.content(repr(e))
        res.status(500)

def handler(req,res,param):
    findall(req,res,param)

