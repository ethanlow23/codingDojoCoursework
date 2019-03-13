# Making and Reading Dictionaries
aboutMe = {
    'name' : 'Ethan',
    'age' : '27',
    'country' : 'US',
    'language' : 'Chinese'
}

def print_dict(dict):
    for i in dict:
        print 'my {} is {}'.format(i, dict[i])
print_dict(aboutMe)