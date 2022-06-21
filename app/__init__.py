# -*- coding: utf8 -*-
import flasgger
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string

from faker import Faker
from loguru import logger
from flasgger import Swagger

from config import envs
from modules.utils import CustomJSONEncoder

fake = Faker(['ja_JP'])

db = SQLAlchemy()

app = Flask('__name__')

# 注册蓝图 (蓝图路径:app, 蓝图路由)
# (app.api.test:app, /api/test)
blueprints = [
    ('app.home.index:app', '/'),
    ('app.api.test:app', '/api/test'),
]
for blueprint in blueprints:
    try:
        app.register_blueprint(import_string(blueprint[0]), url_prefix=blueprint[1])
    except Exception as e:
        app.logger.warning(e)

# 配置基础参数
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

# 挂接 loguru 日志对象
app.logger = logger

# 替换默认的JSON编码器
app.json_encoder = CustomJSONEncoder

# 数据库默认URL
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4".format(**envs.mysql)

# 输出 SQLAlchemy 信息
app.config['SQLALCHEMY_ECHO'] = False

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 数据库连接池的大小
app.config['SQLALCHEMY_POOL_SIZE'] = 10

# 自动回收连接的秒数。这对 MySQL 是必须的，默认 情况下 MySQL 会自动移除闲置 8 小时或者以上的连接。 需要注意地是如果使用 MySQL 的话， Flask-SQLAlchemy 会自动地设置这个值为 2 小时。
app.config['SQLALCHEMY_POOL_RECYCLE'] = 60 * 10

# 绑定多个数据库，官方文档:http://www.pythondoc.com/flask-sqlalchemy/binds.html
# app.config['SQLALCHEMY_BINDS'] = {}

CORS(app, supports_credentials=True)

db.init_app(app)

swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['title'] = "开发者接口文档"  # 配置大标题
swagger_config['description'] = "开发者接口文档"  # 配置公共描述内容
# swagger_config['host'] = "127.0.0.1:5000"  # 请求域名
Swagger(app=app, config=swagger_config)
