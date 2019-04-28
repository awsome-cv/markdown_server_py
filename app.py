#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bson.json_util import dumps
from flask import Flask,Blueprint
from flask import make_response
from flask_restful import reqparse, Api, Resource
from NoteServices import Note
from UserServices import User
from flask_docs import ApiDoc

def output_json(obj, code, headers=None):
    """
    This is needed because we need to use a custom JSON converter
    that knows how to translate MongoDB types to JSON.
    """
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})

    return resp
DEFAULT_REPRESENTATIONS = {'application/json': output_json}
app = Flask(__name__)


ApiDoc(app)
api = Api(app)
api.representations = DEFAULT_REPRESENTATIONS



parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('email')
parser.add_argument('password')
parser.add_argument('note')



# GetYourPasswordBack!
# Send You An Email via dong.wangdongdong.xyz
@api.resource('/getBack')
class getBack(Resource):
    """找回密码"""
    def post(self):
        """通过用户名与注册时使用的邮箱找回用户密码

        Args:
            {
            ”name“：name,
            "email":email
            }

        Returns:
            An email will be sent to user's email!

        """
        args = parser.parse_args()
        user_name=args['name']
        user_email=args['email']
        print(user_email)
        user = User()
        return user.back(user_name,user_email)

# 登陆
# 根据用户名和密码验证登陆
@api.resource('/login')
class UserLogin(Resource):
    """用户登陆"""
    def post(self):
        """通过用户名与密码登陆

        Args:
            {
            ”name“：name,
            "password":password
            }

        Returns:
            登陆成功：[true,
                    {
                     "_id": {
                            "$oid": "用户_id"
                            },
                        "name": "用户名",
                        "email": "用户名",
                        "password": "用户密码"
                    }
                    ]
            登陆失败：[ false ]

        """
        args = parser.parse_args()
        user_name=args['name']
        user_password=args['password']
        user = User()
        return user.login(user_name,user_password)

# 注册
# 根据用户名、密码和邮箱进行注册
@api.resource('/signup')
class UserSignup(Resource):
    """用户注册"""
    def post(self):
        """通过用户名、密码和邮箱进行注册

                Args:
                    {
                    ”name“：name,
                    "password":password
                    ”email“:email
                    }

                Returns:
                    成功："成功"
                    失败："注册失败"

                """
        args = parser.parse_args()
        user_name=args['name']
        user_password=args['password']
        user_email=args['email']
        user = User()
        return user.create(user_name,user_email,user_password)




class NoteOptions(Resource):
    """管理用户的笔记"""
    def get(self,owner_id):
        """通过用户的_id,获取owner_id==_id的所有笔记

                   Args:
                       <owner_id>
                   Returns:
                       成功：该用户下所有的笔记[]
                       失败：[]

                   """
        _note=Note()
        return _note.getAll(owner_id)

    def delete(self,_id):
        """通过笔记的_id,删除对应笔记

                    Args:
                        /delete/<_id>
                    Returns:
                        成功：[True]
                        失败：[False]

                    """
        _note = Note()
        print(_id)
        return  _note.deleteOne(_id)

    def put(self):
        """通过笔记的_id,更新对应笔记

                        Args:
                            {"note":NEW_NOTE}
                        Returns:
                            成功：[True]
                            失败：[False]

                        """
        args = parser.parse_args()
        note = json.loads(args['note'].replace("'", "\""))
        _note = Note()
        return _note.updateOne(note)
    def post(self):
        """创建新对应笔记

                           Args:
                               {NEW_NOTE}
                           Returns:
                               成功：[True]
                               失败：[False]

                           """
        args = parser.parse_args()
        print(args['note'])
        note=json.loads(args['note'].replace("'", "\""))
        _note = Note()
        return _note.createOne(note['title'],note['owner_id'],note['contains'],note['edit_date'],)



api.add_resource(NoteOptions,
    '/notes/<owner_id>',
    '/notes/delete/<_id>',
    '/notes')




if __name__ == '__main__':
    app.run(debug=True)