import pymysql
import pymysql.cursors
from dbutils.pooled_db import PooledDB
import json
from website.index import get_config

def find(req,res,param):
    try:
        if req.has_form("id"):
            config = get_config()
            pool = PooledDB(pymysql,cursorclass=pymysql.cursors.DictCursor,host=config['host'],port=config['port'], user=config['username'], password=config['password'],database=config['database'],charset=config['charset'])
            connection = pool.connection()
            cur = connection.cursor()
            cur.execute("SELECT * FROM `websites` WHERE `id`=%s;" , (int(req.get_form('id'))))
            result = cur.fetchone()
            cur.close()
            connection.close()
            res.header('Content-Type','application/json')
            res.content(json.dumps(result,ensure_ascii=False))
            res.status(200)
    except Exception as e:
        res.content(repr(e))
        res.status(500)

def handler(req,res,param):
    find(req,res,param)

