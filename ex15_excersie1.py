# coding:utf-8
# 只是用raw_input写这个脚本
file_name = raw_input("Please input your file name")
txt = open(file_name)

print "Here's your file %r." % file_name
print txt.read()

print "The script is closed."
txt.close()

# 这种得到文件名的方法更好，减少了名称的传递步骤
