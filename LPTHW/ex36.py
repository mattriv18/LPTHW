from sys import exit
knife = False

def start():
    print "You wake up in a dark room."
    print "The air is cold and your face is covered in dust from the ground."
    print "You see a small sink with a mirror and an old wooden door."

    next = raw_input('Where should you go? ')

    print "-" * 15

    if next == 'door':
        hallway_room()
    elif next == 'sink':
        sink()
    else:
        print "-" * 15
        print "Try \'door\' or \'sink\'"
        start()

def sink():
    print "You get up to the sink and turn the water on."
    print "You wet your hands and try to wash the dirt off your face."
    print "As you open your eyes a monster jumps out of the mirror."
    death('The monsters proceeds to eat your face off.')

def hallway_room():
    print "As you walk through the door, you see a long hallway."
    print "There are two rooms on either side of the hallway,"
    print "And one at the end of the hallway."

    next = raw_input('Where should you go? ')
    print "-" * 15

    if next == 'left':
        death("You walk into the room to instantly be exploded")
    elif next == 'end':
        print "You feel a sting in your neck and you black out"
        print "-" * 15
        start()
    elif next == 'right':
        kitchen_room()
    else:
        print "-" * 15
        print "Try \'left\', \'right\', or \'end\'"
        hallway_room()

def kitchen_room():
    print "You open the door to enter into the kitchen of the home."
    print "There are many drawers, an oven that is rusted over and open,"
    print "and a door that when you try to open it is locked."

    kitchen_door = False

    while True:
        next = raw_input('Where should you go? ')
        print "-" * 15

        if next == "drawers":
            print "You find a knife in the drawer and you take it."
            knife = True
        elif next == "door" and not kitchen_door:
            print "The door is locked!"
        elif next == "oven":
            print "You search the rusted oven to see a key,"
            print "stuck inside the oven and you manage to pry it out"
            kitchen_door = True
        elif next == "door" and kitchen_door:
            living_room()
            break
        else:
            print "-" * 15
            print "Try \'drawers\' or \'oven\'"

def living_room():
    print "You use the key to open the door, but as you open it you hear,"
    print "footsteps in the room. There is no turning back now."
    print "The room is dark so you can sneak around."
    print "The couch could hide you from him or you could take your chances in a fight"

    next = raw_input('What should you do? ')
    print "-" * 15

    if next == 'couch':
        couch()
    elif next == 'fight' and knife:
        end()
    elif next == 'fight' and not knife:
        death('The man turns around and is actually a bear and kills you.')
    else:
        print "-" * 15
        print "Try \'couch\' or \'fight\'"
        living_room()

def couch():
    print "You quickly rush to the couch and crouch down behind it."
    print "However the mans footsteps suddenly stop and he starts walking"
    print "Slowly towards the couch that you are behind."
    print "However instead of finding you, he just sits down instead."

    if knife == True:
        next = raw_input('What should you do? ')
        print "-" * 15
        if next == 'knife':
            end()
        elif next =='talk':
            death('The man turns around and is actually a bear and kills you.')
        else:
            print "-" * 15
            print "Try \'knife\' or \'talk\'"
            couch()
    elif knife == False:
        next = raw_input('What should you do? ')
        print "-" * 15
        if next == 'fight':
            end()
        elif next == 'talk':
            death('The man turns around and is actually a bear and kills you.')
        else:
            print "-" * 15
            print "Try \'talk\' or \'fight\'"
            couch()

def end():
    print "The man turns around and is actually a bear. However as he stands up,"
    print "he trips and falls over the rug, you go in for your oppurtunity and"
    print "get him. However as you fight him candy starts flowing out of his wounds."
    print "Turns out he is actually just a pinata."
    exit(0)


def death(why):
    print why, "Good Job!"
    exit(0)

start()
