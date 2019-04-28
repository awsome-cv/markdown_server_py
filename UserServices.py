from UserDBModel import Users
from sendMail import email
class User():
    def login(self,user_name,user_password):
        user = Users(user_name,'',user_password)
        res = user.login()
        return res

    def create(self,user_name, user_email,user_password):
        user = Users(user_name, user_email,user_password)
        res = user.save()
        if(res):
            return "成功",200
        else:
            return "注册失败",201

    def back(self,user_name,user_email):
        user = Users(user_name,user_email,"")
        res = user.back()
        print((res[1]))
        if(res[0]):
            _email = email()
            return _email.mail(res[1],"Password:"+res[2])