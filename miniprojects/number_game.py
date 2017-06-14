from random import randint

print "Try to guess my number from 1 to 100"

number = randint(0,100)

def game():
    guess = int(raw_input('> '))

    if guess > number:
        print "Too High!"
        game()
    elif guess < number:
        print "Too Low!"
        game()
    else:
        print "You got it!"

game()
