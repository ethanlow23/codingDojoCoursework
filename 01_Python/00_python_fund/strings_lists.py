# Find and Replace
words = "it's thanksgiving day. it's my birthday, too!"
print words.find('day')

new_words = words.replace('day', 'month')
print new_words

# Min and Max
x = [2,54,-2,7,12,98]
print min(x), max(x)

# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[-1]

new_x = [x[0], x[-1]]
print new_x

# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
second_half = x[len(x) / 2:]
first_half = x[: len(x) / 2]
second_half.insert(0, first_half)
print second_half
