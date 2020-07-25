from hi import hi
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

app = hi()


@app.route(r'^/home/?$', ['GET'])
def home(req, res, param):
    from home import index
    index.handler(req, res, param)


@app.route(r"^/post/(?P<id>\d+)?$", ['GET', 'POST'])
def post(req, res, param):
    from post import index
    index.handler(req, res, param)


@app.route(r"^/edit/?$", ['GET'])
def edit(req, res, param):
    from edit import index
    index.handler(req, res, param)


@app.route(r'^/login/?$', ['GET'])
def login(req, res, param):
    from login import index
    index.handler(req, res, param)


@app.route(r'^/logout/?$', ['GET'])
def logout(req, res, param):
    from logout import index
    index.handler(req, res, param)


def main(req, res):
    app.run(req, res)
