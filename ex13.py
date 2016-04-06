#coding:utf-8
#读取文件
#open方法
from sys import argv
script, filename = argv
txt = open(filename)

#read方法
print "Here is your file %r:"% filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")


txt_again = open(file_again)

#<built-in method read of file object at 0x00000000025A8C00>
print txt_again.read
