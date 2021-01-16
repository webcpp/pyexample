def handler(req,res,param):
    res.header('Content-Type','text/plain;charset=utf-8')
    res.content(param['module']+' Not Found\n')
    res.status(404)