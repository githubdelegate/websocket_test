from . import api
from flask import jsonify


# 获取用户的好友列表
@api.route('/user/friends/')
def friends():
    d = {'error': 0, 'result': ['zy', 'nj']}
    return jsonify(d)