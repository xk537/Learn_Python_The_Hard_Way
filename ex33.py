def num_print(n):
    i = 0
    numbers = []
    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)
        i +=1
        print "Numbers now: " , numbers
        print "At the bottom i is %d" % i
    print "The numbers: "

    for num in numbers:
        print num

num_print(7)
