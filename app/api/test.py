# -*- coding: utf8 -*-
from flask import request
from flask import jsonify
from flask import Blueprint

app = Blueprint('/api/test', __name__)


@app.route('/', methods=['GET'])
def get():
    """
    获取数据
    ----
    tags:
        - test
    parameters:
        - name: id
          in: query
          type: integer
          format: int64
          required: true
    responses:
        200:
            description: 成功
            schema:
                type: object
                properties:
                    code:
                        type: integer
                        example: 200
                    msg:
                        type: string
                        example: ok
                    data:
                        type: object
        400:
            description: 失败
            schema:
                type: object
                properties:
                    code:
                        type: integer
                        example: 400
                    msg:
                        type: string
                        example: msg
    """

    return jsonify(code=200, msg='ok', endpoint=request.endpoint)


@app.route('/list', methods=['GET'])
def lists():
    """
    获取数据列表
    ----
    tags:
        - test
    responses:
        200:
            description: ok
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                        data:
                            type: string
                            example: data
    """

    return jsonify(code=200, msg='ok', endpoint=request.endpoint)


@app.route('/', methods=['POST'])
def post():
    """
    添加数据
    ----
    tags:
        - test
    parameters:
        - name: body
          in: body
          description: body
          required: true
          schema:
            id: 添加数据
            required:
                - data
            properties:
                data:
                    type: string
                    description: data
                    example: data
    responses:
        200:
            description: 成功
            schema:
                type: object
                properties:
                    code:
                        type: integer
                        example: 200
                    msg:
                        type: string
                        example: ok
        400:
            description: 失败
    """

    return jsonify(code=200, msg='ok', endpoint=request.endpoint)


@app.route('/', methods=['PUT'])
def put():
    """
    修改数据
    ----
    tags:
        - test
    parameters:
        - name: body
          in: body
          description: body
          required: true
          schema:
            required:
                - id
            properties:
                id:
                    type: integer
                    example: 1
                data:
                    type: string
                    example: data
    """

    return jsonify(code=200, msg='ok', endpoint=request.endpoint)


@app.route('/', methods=['DELETE'])
def delete():
    """
    删除数据
    ---
    tags:
        - test
    parameters:
        - name: id
          in: query
          type: integer
          format: int64
          required: true
    responses:
        200:
            description: 成功
            schema:
                type: object
                properties:
                    code:
                        type: integer
                        example: 200
                    msg:
                        type: string
                        example: ok
        400:
            description: 失败
            schema:
                type: object
                properties:
                    code:
                        type: integer
                        example: 400
                    msG:
                        type: string
                        example: error
    """

    return jsonify(code=200, msg='ok', endpoint=request.endpoint)
