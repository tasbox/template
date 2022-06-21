"""
    开发环境配置
"""
import os

flask = {
    'host': '127.0.0.1',
    'port': 5000,
    'workers': os.cpu_count() * 2 + 1,
    'threads': 1,
    'reload': True,
    'daemon': False,
    'accesslog': 'logs/gunicorn.access.log',
    'errorlog': 'logs/gunicorn.error.log'
}

mysql = {
    'host': '192.168.19.36',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'database': 'template'
}
