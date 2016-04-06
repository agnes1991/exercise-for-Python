#coding:utf-8
#提示和传递
#调用的时候，同时输入参数
from sys import argv

#提示符设置为变量 prompt
script, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s script."%(script, user_name)
print "I'd like to ask you a few questions."
print "Do you like me %s?"% user_name
likes = raw_input(prompt)

print "Where do you lives %s?"% user_name
lives = raw_input(prompt)

print "What kind of computer %s do you have?"% user_name
computer = raw_input(prompt)

print """
Alright, you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
"""% (likes, lives, computer)