#coding:utf-8
#字符串和文本
#定义x、binary、y
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#y取binary和do_not的值
y = "Those who knows %s and those who %s." %(binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
#%r是干嘛的？？？
joke_evalution = "Isn't that joke so funny?! %r"

print joke_evalution % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
