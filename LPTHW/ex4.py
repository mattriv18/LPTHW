#How many cars we got today
cars = 100

#How many people can fit in a car
space_in_a_car = 4.0

#Amount of drivers we have today
drivers = 30

#Amount of people we have to put in cars today
passengers = 90

#Amount of cars we arent gonna drive today
cars_not_driven = cars - drivers

#Amount of cars going out based on the drivers we have
cars_driven = drivers

#Total people we can transfer today
carpool_capacity = cars_driven * space_in_a_car

#Amount of passengers that can fit in each car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"
