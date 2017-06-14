def is_integer(input):
    bool_list = [] # to hold the b
    truth = True
    for i in input:
        # tests if i is an integer, records the boolean in bool_list
        bool_list.append(i in str(range(0, 10)))
    for t in bool_list:
        truth = truth and t # 'adds' each boolean in bool_list
    print truth # True if all are integers, False if not.
    print bool_list

is_integer("1p23p")
