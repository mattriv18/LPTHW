my_name = 'Matthew J. Rivera'
my_age = 17
my_height = 65 #inches
my_weight = 165.5 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

#The %s or %d becomes a variable that is
#embedded into the string itself, string being
#what is between the quotations.
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Good thing I am losing weight."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are mostly %s dending on brushing." %my_teeth

print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

#  %s = string
#  %d = number
#  %r = debugging
