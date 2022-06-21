# -*- coding: utf8 -*-
from flask import request
from flask import jsonify
from flask import Blueprint

app = Blueprint('/home/index', __name__)


@app.route('/', methods=['GET', 'POST'])
def get():
    """"""
    return 'ok'
