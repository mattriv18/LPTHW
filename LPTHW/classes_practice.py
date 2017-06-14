class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.customers_served = 0

    def describe_restaurant(self):
        print "The restaurant's name is " + self.restaurant_name + "."
        print "The restaurant makes " + self.cuisine_type + " food."

    def set_number_served(self, served):
        self.customers_served = served

        print "Number of customers served: " + str(self.customers_served)

    def increment_number_served(self, increment):
        self.customers_served += increment

        print "Number of customers served: "  + str(self.customers_served)

    def open_restaurant(self):
        print "Restaurant is open."

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = ['Chocolate', 'Vanilla', 'Strawberry']

    def DisplayFlavors(self):
        print "We have the flavors: " + self.flavors[0] + self.flavors[1] + self.flavors[2]


Carvel = IceCreamStand("Carvel", "Ice Cream")
Chipotle = Restaurant("Chipotle", "Mexican")

Carvel.describe_restaurant()
Carvel.open_restaurant()
Carvel.DisplayFlavors()
print "-" * 10
Chipotle.describe_restaurant()
Chipotle.open_restaurant()
Chipotle.set_number_served(500)
Chipotle.increment_number_served(50)
