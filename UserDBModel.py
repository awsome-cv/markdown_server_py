#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo

# 返回一个 collection
def get_coll():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.markdown_py
    user = db.users
    return user


class Users(object):

    def __init__(self, name, email,password):
        self.name = name
        self.email = email
        self.password = password



    def save(self):
        user = {"name": self.name, "email": self.email, "password": self.password}
        coll = get_coll()
        res=coll.find_one({"name":self.name})
        if((res)):
            return False
        else:
            coll.insert(user)
            return True

    def login(self):
        user = {"name": self.name,  "password": self.password}
        coll = get_coll()
        res = coll.find_one(user)
        if((res)):
            return [True, res]
        else:
            return [False]

    def back(self):
        user = {"name": self.name,  "email": self.email}
        coll = get_coll()
        res = coll.find_one(user)
        if((res)):
            if(res['email']==user['email']):
                return [True,res['email'],res['password']]
        else:
            return [False]
    @staticmethod
    def query_users():
        users = get_coll().find()
        return users

