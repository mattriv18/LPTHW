import random

def problem(tests):

    test_truth = True
    test_amount = 0

    while test_truth:
        prizes = ["goat1", "car", "goat2"]
        doors = [prizes[0], prizes[1], prizes[2]]

        random.shuffle(doors)

        choose1 = int(raw_input("Which door?\n> "))

        if choose1 == 1:
            choose1 = 0
        elif choose1 == 2:
            choose1 = 1
        elif choose1 == 3:
            choose1 = 2
        print choose1
        print doors

        montychoice = random.choice(doors)

        while True:
            if doors.index(montychoice) == choose1:
                montychoice = random.choice(doors)
            elif montychoice == 'car':
                montychoice = random.choice(doors)
            else:
                break

        print "Behind door number %d is a %s" % (doors.index(montychoice) + 1, montychoice)
        doors.remove(montychoice)
        print doors

        print "Would You like to switch to a different door?"

        choose2 = raw_input("> ")

        if choose1 == 2:
            choose1 -= 1
        else:
            pass

        print doors
        if choose2 == 'yes':
            doors.remove(doors[choose1])
            print "You switched your door and got a %s" % doors[0]
        elif choose2 == 'no':
            print "You did not switch your door and got a %s" % doors[choose1]

        if test_amount < tests:
            test_amount += 1
        elif test_amount == tests:
            results()





problem(1000)
