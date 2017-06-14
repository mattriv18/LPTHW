## Animal is-a object
class Animal(object):
    pass

## Dog is-a object that is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## That has-a __init__ function with parameters self and name
        ## The Dog has-a name
        self.name = name

## Cat is-a object that is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## That has-a __init__ function with parameters self and name
        ## The cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## That has-a __init__ function with parameters self and name
        ## The person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## An employee is-a object that is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
        ## An employee has-a salary
        self.salary = salary

## A fish is-a object
class Fish(object):
    pass

## A salmon is-a object that is-a Fish
class Salmon(Fish):
    pass

## A Halibut is-a object that is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet satan
mary.pet = satan

## Frank is-a Employee that has-a name Frank and has-a salary 120000
frank = Employee("Frank", 120000)

## Frank has-a pet rover
frank.pet = rover

## A flipper is-a fish
flipper = Fish()

## A crouse is-a salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()
