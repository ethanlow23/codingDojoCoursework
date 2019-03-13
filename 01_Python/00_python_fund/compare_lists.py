def compare_lists(lst1, lst2):
    if len(lst1) != len(lst2):
        print 'the lists are not the same'
    else:
        for i in range(0, len(lst1)):
            if lst1[i] == lst2[i]:
                
            else:
                print 'the lists are not the same'
                
'''
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
'''
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

compare_lists(list_one, list_two)