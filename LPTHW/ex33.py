i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers

    print "At bottom i is %d" % i
    print "------------"
print "The numbers: "

for num in numbers:
    print num
