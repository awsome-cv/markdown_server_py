#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
from bson.objectid import ObjectId
# 返回一个 collection
def get_coll():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.markdown_py
    note = db.notes
    return note


class Notes(object):



    def __init__(self, title, owner_id, contains, edit_date,):
        self.title = title
        self.owner_id = owner_id
        self.contains = contains
        self.edit_date = edit_date

    def getOne(self,_id,owner_id):
        coll = get_coll()
        res = coll.find({"_id": ObjectId(_id),"owner_id":owner_id})
        return res

    def create(self):
        note = {"title": self.title, "owner_id": self.owner_id, "contains": self.contains, "edit_date": self.edit_date}
        coll = get_coll()
        res=coll.insert_one(note)
        return [True]

    def delete(self,_id):
        note = {"_id": ObjectId(_id)}
        coll = get_coll()
        res = coll.remove(note)
        print(res)
        return [res]
    def update(self,note):
        coll = get_coll()
        res = coll.update_one({"_id": ObjectId(note['_id'])},{"$set":{ "contains":  note['contains'],
        "edit_date": note['edit_date']}})
        return [note]

    def getAll(self,owner_id):
        coll = get_coll()
        res = coll.find({"owner_id":owner_id})
        return  res


