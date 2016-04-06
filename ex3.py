#coding:utf-8
#变量和命名
###定义车辆、空间、司机、乘客等的数量
cars = 100				#车辆,常量
space_in_a_car = 4.0	#空间,常量
drivers = 30			#司机,常量
passengers = 90			#乘客,常量
cars_not_driven = cars-drivers		#不使用的车辆，变量
cars_driven = drivers				#在使用的车辆，变量
carpool_capacity = cars_driven*space_in_a_car			#停车场剩余空间，变量
average_passengers_per_car = passengers/cars_driven		#每辆车平均乘客数量，变量

#打印
print "There are ", cars,"cars available."
print "There are only ",drivers,"drivers available."
print "There will be ",cars_not_driven,"empty cars today."
print "We can transport ",carpool_capacity,"people today."
print "We have ",passengers,"to transport today."
print "We need to put about ",average_passengers_per_car,"passengers in each car."
