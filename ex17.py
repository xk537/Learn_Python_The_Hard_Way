#coding:utf-8
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file,to_file))

# We could do this two on one line too,how?
input_ = open(from_file)
indata = input_.read()

print ("Does the output file exist? %r" % exists(to_file))
print ("Ready,hit RETURN to continue, CRT-C to abort.")
input()

output = open(to_file,'w')
output.write(indata)

print ("Alright,all done.")

output.close()
input_.close()
