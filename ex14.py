# coding:utf-8

from sys import argv
script, user_name, script_age = argv
prompt = '>'

print "Hi %s, this is %s script,it is %s years old. "
% (user_name, script, script_age)
print "I'd like to ask you some questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live in %r. Not sure where that is.
And you have a %s computer. Nice.
""" % (likes, lives, computer)
