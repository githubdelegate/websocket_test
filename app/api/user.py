from . import api
from flask import jsonify


# 获取用户的好友列表
@api.route('/user/friends/')
def friends():
    d = {'error': 0, 'result': ['zy', 'nj', '哈哈']}
    return jsonify(d)