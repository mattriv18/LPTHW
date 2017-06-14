x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

#printing the variable 'x' and 'y' which are strings
print x
print y

#putting the string 'x' inside of the '%r' variable/formatter
print "I said: %r." % x
#putting the string 'y' inside of the '%s' variable/formatter
print "I also said: '%s'." % y

#defining hilarious as false
hilarious = False
#creating a new variable that is a string without a defined
#formatter value
joke_evaluation = "Isn't that joke so funny?! %r"

#printing the joke_evaluation variable but then actually
#assigning a value to the formatter which is the variable
#hilarious
print joke_evaluation % hilarious

#defining variables with adding two strings together
w = "This is the left side of..."
e = "a string with a right side"
print w + e
