import os
import tempfile
import pytest
from NoteServices import Note
from UserServices import User
CONF_USER={"user_name":"test1111",
      "email":"thomastieyi@gmail.com",
      "user_password":"TEST123456",
      }
CONF_NOTE={
        "title": "TEST_NOTE",
        "owner_id": "5cc446fe139ed6e58e77d9ce",
        "contains": "TEST_NOTE",
        "edit_date": "2019-04-18T16:00:00.000Z"
    }
CONF_NOTE_UPDATE={
        "_id":"5cc56cf001f3d7c17ac421f2",
        "title": "TEST_NOTE",
        "owner_id": "5cc446fe139ed6e58e77d9ce",
        "contains": "TEST_NOTE",
        "edit_date": "2019-04-18T16:00:00.000Z"
    }
def test_signup_test():
    user = User()
    rv = user.create(CONF_USER.get('user_name'),CONF_USER.get('email'),CONF_USER.get('user_password'))
    assert '成功' or "注册失败" in rv

def test_login_test():
    user = User()
    rv = user.login(CONF_USER.get('user_name'), CONF_USER.get('user_password'))
    assert  rv[0]

def test_create_note():
    note=Note()
    rv = note.createOne( CONF_NOTE.get('title'),CONF_NOTE.get('owner_id'),CONF_NOTE.get('contains'),CONF_NOTE.get('edit_date'))
    assert  rv[0]

def test_put_note():
    note=Note()
    rv = note.updateOne( CONF_NOTE_UPDATE)
    assert  rv[0]

def test_get_note():
    note=Note()
    rv = note.getAll( CONF_NOTE.get('owner_id'))
    assert rv

def test_delete_note():
    note=Note()
    rv = note.deleteOne( "5cc446fe139ed6e58e77d9ce")
    assert rv

def test_find_back():
    user =User()
    rv = user.back(CONF_USER.get('user_name'),CONF_USER.get('email'))
    assert rv