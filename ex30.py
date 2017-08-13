#coding:utf-8

people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take cars."
elif cars < people:
    #多分支，第一个elif后的条件成立时，程序不在对其他分支进行判断
    #节省资源
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright,let's just take the buses."
else:
    print "Fine,let's stay home then."
