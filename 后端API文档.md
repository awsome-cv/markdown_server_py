# Getback(找回密码)

## POST(通过用户名与注册时使用的邮箱找回用户密码)

#### url

- /getBack

#### doc

```
        Args:
            {
            ”name“：name,
            "email":email
            }

        Returns:
            An email will be sent to user's email!
```

# Noteoptions(管理用户的笔记)

## DELETE(通过笔记的\_id,删除对应笔记)

#### url

- /notes

#### doc

```
                    Args:
                        /delete/<_id>
                    Returns:
                        成功：[True]
                        失败：[False]
```

## GET(通过用户的\_id,获取 owner_id==\_id 的所有笔记)

#### url

- /notes

#### doc

```
                   Args:
                       <owner_id>
                   Returns:
                       成功：该用户下所有的笔记[]
                       失败：[]
```

## POST(创建新对应笔记)

#### url

- /notes

#### doc

```
                           Args:
                               {NEW_NOTE}
                           Returns:
                               成功：[True]
                               失败：[False]
```

## PUT(通过笔记的\_id,更新对应笔记)

#### url

- /notes

#### doc

```
                        Args:
                            {"note":NEW_NOTE}
                        Returns:
                            成功：[True]
                            失败：[False]
```

# Userlogin(用户登陆)

## POST(通过用户名与密码登陆)

#### url

- /login

#### doc

```
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
```

# Usersignup(用户注册)

## POST(通过用户名、密码和邮箱进行注册)

#### url

- /signup

#### doc

```
                Args:
                    {
                    ”name“：name,
                    "password":password
                    ”email“:email
                    }

                Returns:
                    成功："成功"
                    失败："注册失败"
```
