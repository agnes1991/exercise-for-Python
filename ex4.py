#coding:utf-8
##ex4
my_name = 'Zed A. Shaw'		#姓名
my_age = 35  # not a lie	#年龄
my_height = 74 #inches		#身高
my_weight = 180  # lbs		#体重
my_eyes = 'Blue'			#眼睛颜色
my_teeth = 'White'			#牙齿颜色
my_hair = 'Brown'			#头发颜色

print "Let's talk about %s." % my_name
print "He is %d inches tall." % my_height
print "He is %d prounds heavy." % my_weight
print "Actually that is not too heavy."
print "He's got %s eyes and %s hair."%(my_eyes,my_hair)
print "He's teeth is usually %s depending on the coffee." %my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d."%(my_age, my_height, my_weight,my_age + my_height + my_weight)
