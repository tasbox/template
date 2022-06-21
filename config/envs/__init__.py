import os

# 创建日志目录
if not os.path.exists('logs'):
    os.mkdir('logs')

ENV_MASTER = 'MASTER'
ENV_DEVELOP = 'DEVELOP'
ENV_NAME = os.getenv('ENV_NAME', ENV_DEVELOP)

if ENV_NAME == ENV_MASTER:
    from .master import *
if ENV_NAME == ENV_DEVELOP:
    from .develop import *
