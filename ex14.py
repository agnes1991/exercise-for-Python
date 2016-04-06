#coding:utf-8
#读写文件
#运行时先输入将要新建文件的名称及类型（test.txt）
from sys import argv
script, filename = argv

print "We are going to erase %r. "% filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input ("?")

print "Opening the file..."
target = open(filename, 'w')


#target.truncate(n)从首行首字符开始截断n个字符，截断后面的字符被删除
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#定义line1，line2，line3
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#写入文件
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

#关闭文件，想到于编辑器中的file--save
print "And finally, we close it."
target.close()