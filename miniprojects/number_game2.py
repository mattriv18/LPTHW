import random

print "Pick a number from 0 to 100 and I will try to guess your number"

number = int(raw_input('> '))

guessestaken = 0
high = 100
low = 0

while True:
    guess_range = range(low,high)
    guess = random.choice(guess_range)

    if guess > number:
        print guess
        print guess_range
        high = guess
        guessestaken += 1
    elif guess < number:
        print guess
        print guess_range
        low = guess + 1
        guessestaken += 1
    elif guess == number:
        print guess
        guessestaken += 1
        break

print "Your number is: %d" % guess
print "I guessed it in %d guesses" % guessestaken
print guess_range
