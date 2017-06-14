base = int(raw_input("Length of base? "))
height = int(raw_input("Length of height? "))

def triangle(side1, side2):
    area = side1 * side2 / 2
    print "The area of the triangle is %d" % area

triangle(base, height)
