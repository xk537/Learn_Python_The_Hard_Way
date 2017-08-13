# -*- coding: utf-8 -*-

import random
# random 用于生成一个随机的浮点数
num = random.randint(0,20)
# 用于随机生成20以内的整数

print ("游戏开始")

for i in range(1,11):
    guess_num = int(input("请输入20以内的数字： "))
    n = 10 - i
    if guess_num > num:
        print ("您猜的数字大了！请重新输入20以内数字：\n您还剩{0}次机会".format(n))
    elif guess_num < num:
        print ("您猜的数字小了！请重新输入20以内数字：\n您还剩{0}次机会".format(n))
    else:
        print ("您猜对了！真棒！")
        
