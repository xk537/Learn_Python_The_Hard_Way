# coding: utf-8

filename = raw_input("Please type your filename:\n>")
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "We close your file"
txt.close()
