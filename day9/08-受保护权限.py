"""
受保护权限：只能在类内部和派生类中访问。
说明：python中没有受保护权限的限制
"""


class Person:
    def __init__(self):
        # 受保护权限
        self._name = 'hello'


class Staff(Person):
    def get_name(self):
        print(self._name)


staff = Staff()
staff.get_name()

# print(staff._name)

person = Person()
print(person._name)

# 权限
# public
# protected
# private
