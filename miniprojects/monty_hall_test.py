import random

def problem(tests):

    wins = 0
    losses = 0
    doors = ["goat", "car", "goat"]

    for test in range(tests):
        #we shuffle the doors
        random.shuffle(doors)
        #the player picks a door
        choicenumber = random.randrange(len(doors))
        choice = doors[choicenumber]
        #monty chooses a door
        montychoicenumber = random.randrange(len(doors))
        montychoice = doors[montychoicenumber]

        while montychoice == 'car' and montychoice == choice:
            montychoice = random.choice(doors)

        #if the player's door is a car, he losses
        if choice == 'car':
            losses += 1
            print 'goat'
        elif choice == 'goat':
            wins += 1
            print 'car'

    percentage = (wins * 100) / (wins + losses)
    print "Switching wins: %d" % wins
    print "Switching loses: %d" % losses
    print "Switching wins %d percent of the time" % percentage

problem(1000)
