bottlenumber = range(0,99)
number = 99

#for i in range(0,99):

    #bottlenumber.append(number)

    #number -= 1

for i in bottlenumber:

    print "%d bottles of beer on the wall" % bottlenumber[-1]

    bottlenumber.remove(bottlenumber[-1])

print bottlenumber
