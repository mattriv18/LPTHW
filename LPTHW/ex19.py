# defining the function that we want.
# It also defines the functions variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# We are giving 'cheese_count' and 'boxes_of_crackers' values
# of 20 and 30 and then running the function with those values
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Giving 'cheese_count' and 'boxes_of_crackers' values of a variable
# and then running it on a function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Doing the same thing as the first run of the function
# but this time we are giving them values after the math
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# literally the same thing as the last one but one number value
# in the equation is a variable
print "We can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
