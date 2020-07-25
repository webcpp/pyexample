from hi import template
import os
import sys


def handler(req,res,param):
    param['title']='jinja2 template'
    tpl_engine = template(os.path.join(os.getcwd(),'pyexample/templates/post'))
    res.content(tpl_engine.file_render('b.j2',param))
    res.status(200)