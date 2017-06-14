def squareRoot(x, numGuess):

    guess = x * .5

    for i in range(0, numGuess):
        print guess
        average = (guess + (x / guess)) * .5
        guess = average

    print guess

squareRoot(1003, 10)
