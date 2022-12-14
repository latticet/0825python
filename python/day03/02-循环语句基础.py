"""
# 流程控制
# 顺序执行
# 分支语句
# 循环语句
"""
a = 'A' * 10

"""
while循环语法：

while 条件表达式:  
    代码块(循环体)
    
# 说明：
判断条件表达式的结果是True还是False
条件为真，执行代码块的内容
然后在返回判断条件是否成立，成立重复上面的操作
不成立跳过代码块，代码继续向下执行
"""

# 死循环， 只要条件不成立的机制，把这种情况就叫做死循环
"""
while 1==1:
    print(a)
"""

# 需求：用循环打印5次a变量
# 计数器
i = 0
while i < 5:
    print(a)
    i += 1  # i = i + 1  # 1 2'

print('==' * 20)

i = 1
while i <= 5:
    print(a)
    i += 1
