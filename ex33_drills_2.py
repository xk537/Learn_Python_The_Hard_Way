def num_print(m, n):
    i = 0
    numbers = []
    while i < m:
        print "At the top i is %d" % i
        numbers.append(i)
        i += n
        print "Numbers now: " , numbers
        print "At the bottom i is %d" % i
    print "The numbers: "

    for num in numbers:
        print num

num_print(7, 2)
