"""
1. 怎么自定义异常类
语法：
class NameError(Exception):
    def __str__(self):
        return '异常描述信息'

2. 如何抛出自定义异常类
    raise 异常对象
"""


# 定义关于长度的异常类
class LenError(Exception):
    def __str__(self):
        return '长度不符合规范'


# 用户注册
# 验证用户名长度  6 - 18
# 接收用户名
try:
    username = input('username:')
    if 6 <= len(username) <= 18:
        print('用户名合法')
    else:
        raise LenError()
except LenError as e:
    print(e)
