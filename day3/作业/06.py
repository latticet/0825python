"""
写一个去民政局办理结婚的功能
首先询问是否有办证所需照片，如果没有给出相应的提示；
如果有照片，询问是否12元钱，如果没有给出相应的提示；
如果有12元钱，则办理成功，给出相应的成功提示。
"""
# 设置初始变量
is_pic = int(input('是否有照片【1|0】：'))
money = int(input('钱的数量：'))

if is_pic:
    if money >= 12:
        print('办理成功')
    else:
        print('下次一定')
else:
    print('没有照片，不能办理')
