# checkerboard

'''
* * * *
 * * * *
* * * *
 * * * *
* * * * 
 * * * *
* * * *
 * * * *
 '''
board = ''
for i in range(0, 8):
    if i % 2 == 0:
        for x in range(0, 8):
            if x % 2 == 0:
                board += '*'
            else:
                board += ' '
        board += '\n'
    else:
        for x in range(0, 8):
            if x % 2 == 0:
                board += ' '
            else:
                board += '*'
        board += '\n'
print board