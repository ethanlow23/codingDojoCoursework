# Names: Part I
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def names(dict):
    for i in range(len(students)):
        print students[i]['first_name'] + ' ' + students[i]['last_name']
names(students)

# Names: Part II
users = {
    'Students': [
        {'first_name' :  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}
def students_instructors(dict):
    print 'students'
    for i in range(len(dict['Students'])):
        length = len(dict['Students'][i]['first_name']) + len(dict['Students'][i]['last_name'])
        print str(i+1) + ' - ' + dict['Students'][i]['first_name'] + ' ' + dict['Students'][i]['last_name'] + ' - ' + str(length)
    print 'instructors'
    for i in range(len(dict['Instructors'])):
        length = len(dict['Instructors'][i]['first_name']) + len(dict['Instructors'][i]['last_name'])
        print str(i+1) + ' - ' + dict['Instructors'][i]['first_name'] + ' ' + dict['Instructors'][i]['last_name'] + ' - ' + str(length)
students_instructors(users)