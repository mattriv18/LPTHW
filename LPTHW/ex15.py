#sets argv as a variable to be unpacked
from sys import argv

#sets the amount of variables that argv will unpack
script, filename = argv

#the variable that opens the file that we imported with argv
txt = open(filename)

#says the filename and then reads the opened txt
print "Here's your file %r:" % filename
print txt.read()

txt.close()

#prompts us to type an input to be defined as the variable
print "Type the filename again:"
file_again = raw_input("> ")

#defines the file that we input as a variable
txt_again = open(file_again)

#reads the variable of the text that we input
print txt_again.read()

txt_again.close()
