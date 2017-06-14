import random
import time

responses = ['Outcome is hazy', 'Absolutely', 'Definitely Not',
             'Try Again Later', 'The chances are high!', 'Not Likely!',
             'No Way!', 'No', 'Yes', 'Cannot Predict Now',
             'Try it out and see!']

def inputquestion():

    print "What would you like to ask the magic 8 ball?"

    question = raw_input('> ')

    print "THE MAGIC 8 BALL SAYS..."
    time.sleep(3)

    answer()

def answer():

    print random.choice(responses)
    print "\n Would you like to ask another question?"

    restart = raw_input("[yes or no]>")

    while True:
        if restart == 'yes':
            inputquestion()
            break
        elif restart == 'no':
            print "\nGOODBYE"
            exit(0)
        else:
            print "you must answer yes or no"

def main():
    print "-" * 10
    print "WELCOME TO THE MAGIC 8 BALL"
    print "-" * 10

    inputquestion()

if __name__ == '__main__':
    main()
