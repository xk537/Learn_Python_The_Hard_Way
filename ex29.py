#coding:utf-8

people = 20
cats = 30
dogs = 15

if people < cats:
    # 冒号后面会新建一个代码区段，所以下一行需要缩进，类似函数
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people > dogs:
    print "The world is dry!"

if people < dogs:
    print "The world is drooled on!"

dogs +=5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."
