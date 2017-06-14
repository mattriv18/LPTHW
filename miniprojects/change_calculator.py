from decimal import *

def main():

    enough = True

    while enough:
        print "How much money was given to you?"
        money = float(raw_input('$')) * 100
        print "-" * 10

        print "What is the price of the item?"
        price = float(raw_input('$')) * 100
        print "-" * 10

        if money > price:
            change = money - price
            enough = False
        elif money < price:
            print "The person did not give enough money!!"
            print "-" * 10

    calculator(change)


def calculator(amount_needed):

    coins = [25, 10, 5, 1]
    results = []

    for cointypes in coins:
        change_needed = amount_needed / cointypes
        results.append(change_needed)
        amount_needed -= cointypes * int(change_needed)

    for amount in results:
        if amount < 1:
            amount = 0
        else:
            pass

    end(results)

def end(results):
    print "You need:"
    print "%d quarters" % int(results[0])
    print "%d dimes" % int(results[1])
    print "%d nickels" % int(results[2])
    print "%d pennies" % int(results[3])
    print "-" * 10
    print "Would you like to do another? (yes or no)"

    resettruth = True

    while resettruth:
        reset = raw_input("> ")

        if reset == 'yes':
            resettruth = False
            print "-" * 10
            main()
        elif reset == 'no':
            exit(0)
        else:
            print "You must input yes or no"


if __name__ == "__main__":
    print "-" * 10
    print "WELCOME TO THE CHANGE CALCULATOR"
    print "-" * 10
    main()
