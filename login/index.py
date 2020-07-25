def handler(req,res,param):
    res.header('Content-Type','text/plain;charset=utf-8')
    res.content('login')
    res.status(200)