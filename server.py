# -*- coding: utf8 -*-

import sqlalchemy.exc
from flask import jsonify
from gevent.pywsgi import WSGIServer
from werkzeug.exceptions import HTTPException

from config import envs

from app import app, db, fake


# 全局异常AOP捕获处理
@app.errorhandler(Exception)
def error(e):
    """"""
    app.logger.warning(e)

    # SQLAlchemy 异常
    if isinstance(e, sqlalchemy.exc.SQLAlchemyError):
        return jsonify(code=500, msg=str(e))

    # Flask 异常
    if isinstance(e, HTTPException):
        return jsonify(code=e.code, msg=e.__str__())

    # 默认异常
    return jsonify(code=400, msg=e.__repr__())


if __name__ == '__main__':
    """"""
    host = envs.flask.get('host')
    port = envs.flask.get('port')

    if envs.ENV_NAME == envs.ENV_MASTER:
        WSGIServer((host, port), app).serve_forever()
    else:
        app.run(host, port)
