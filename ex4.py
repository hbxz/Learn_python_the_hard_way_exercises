cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study Drills
# That may because line 7 define "carpool_capacity", not car_pool_capacity, so
# car_pool_capacity is not defined.
# 
# A1: It will be also right. Actually, considering "space_in_a_car" stand for 
# how many people a car can load, maybe integer would be a better type for it. 
# Since we don't load 3.5 people in one car.
# 
# A2: It means it contain info for decimal fraction, and when opreated with 
# integer, it will makes the outcome as floating point number.
# 
# A3: I reject. as well as Q4,5,6.
# 