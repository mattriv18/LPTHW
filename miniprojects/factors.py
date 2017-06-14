def factor(number):

    factors = []

    for testfactor in range(1, number + 1):

        if number % testfactor == 0:
            factors.append(testfactor)
        else:
            pass

    print factors

factor(1234)
