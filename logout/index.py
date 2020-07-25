def handler(req,res,param):
    res.header('Content-Type','text/plain;charset=utf-8')
    res.content('logout')
    res.status(200)