from random import choice

class BaseRoom(object):

    def enter(self):
        print "This is not implemented"
        exit(0)

class Engine(object):
    pass

class SceneHandler(object):
    pass

class Death(BaseRoom):

    def enter(self):
        deaths = ['You have died',
                  'Wasted!',
                  'DEAD!!!!']

        for i in deaths:
            print choice(deaths)
            exit(0)

class MainHallway(BaseRoom):
    pass

class Bathroom(BaseRoom):
    pass

class Kitchen(BaseRoom):
    pass

class Bedroom(BaseRoom):
    pass

a = Death()
a.enter()
