# Odd/Even
def odd_even():
    for i in range(1, 2001):
        if i % 2 == 0:
            print 'num is ' + str(i) + '. this is an even number'
        else:
            print 'num is ' + str(i) + '. this is an odd number'

# Multiply
def multiply(lst, n):
    for i in range(len(lst)):
        lst[i] *= n
    return lst
print multiply([2,4,10,16], 5)

# HackerChallenge
def layered_multiples(lst):
    new_lst = []
    for i in lst:
        temp_lst = []
        for j in range(i):
            temp_lst.append(1)
        new_lst.append(temp_lst)
    return new_lst
print layered_multiples(multiply([2,4,5], 3))