#coding:utf-8
##ex4
my_name = 'Zed A. Shaw'		#����
my_age = 35  # not a lie	#����
my_height = 74 #inches		#���
my_weight = 180  # lbs		#����
my_eyes = 'Blue'			#�۾���ɫ
my_teeth = 'White'			#������ɫ
my_hair = 'Brown'			#ͷ����ɫ

print "Let's talk about %s." % my_name
print "He is %d inches tall." % my_height
print "He is %d prounds heavy." % my_weight
print "Actually that is not too heavy."
print "He's got %s eyes and %s hair."%(my_eyes,my_hair)
print "He's teeth is usually %s depending on the coffee." %my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d."%(my_age, my_height, my_weight,my_age + my_height + my_weight)
