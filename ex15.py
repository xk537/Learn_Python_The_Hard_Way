#coding:utf-8

from sys import argv # 试用python自己的sys模块向程序里面传递参数

script, filename = argv # 将传递进程序的参数赋值给变量 script 和 filename

txt = open (filename) # 打开文件，并将打开的文件赋值给变量 txt

print "Here's your file %r :" % filename # 打印  Here's your file  :   其中%r是字符格式
print txt.read() #读取打开的文件
print "Type the filename again:"  # 打印Type the filename again:
file_again = raw_input(">")  # 引入向程序输入内容的提示符号 > ，并将输入的内容赋值给变量 file_name

txt_again = open(file_again) # 打开上一步输入名称对应的文件，并将结果赋值给变量 txt_again

print txt_again.read() # 读取上一步打开的文件内容

txt.close()

# 用命令行打开文件
# print open('ex15_sample.txt').read()
