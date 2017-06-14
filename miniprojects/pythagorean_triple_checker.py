from sys import exit

def checker():
    sides = []
    print "-" * 10
    print "Type in the side lengths."

    while len(sides) != 3:
        side_input = raw_input("> ")

        if side_input.isdigit():
            sides.append(side_input)
        elif side_input == "exit":
            exit(0)
        else:
            print "You must write a number or type exit"

    sides = [int(i) for i in sides]
    hypotenuse = max(sides)
    sides.remove(hypotenuse)
    c = hypotenuse
    b = sides[1]
    a = sides[0]

    if a**2 + b**2 == c**2:
        print "%d, %d, and %d are a pythagorean triple." % (a, b, c)
        question()
    else:
        print "%d, %d, and %d are not a pythagorean triple." % (a, b, c)
        question()

def question():
    print "Would you like to try another or exit?"
    print "Type exit to exit or just press enter to try another."

    while True:
        answer = raw_input("> ")

        if answer == '':
            checker()
        elif answer == 'exit':
            exit(0)
        else:
            print "Press enter or type exit"

def main():
    print "-" * 10
    print "HELLO WELCOME TO PYTHAGOREAN TRIPLE CHECKER"
    print "\'exit\' can be typed anytime to exit."
    checker()


if __name__ == "__main__":
    main()
