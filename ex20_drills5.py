#coding:utf-8

from sys import argv

script, input_file = argv

def print_a_ine(line_count,f):
    print line_count, f.readline()

current_file = open(input_file)
print "Let's print four lines:\n"

current_line = 1
print_a_ine(current_line,current_file)

current_line += 1
print_a_ine(current_line,current_file)
