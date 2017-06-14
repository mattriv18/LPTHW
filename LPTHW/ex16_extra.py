from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, it RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, "w+")

print "Are you sure you want to delete this file?"
print target.read()

raw_input("?")

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally we close it."
target.close()
