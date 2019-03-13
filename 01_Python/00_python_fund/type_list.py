# Type List
# l = ['magical unicorns',19,'hello',98.98,'world']
# l = [2,3,1,7,4,12]
l = ['magical','unicorns']

lst_type = ''
newStr = 'String:'
total = 0
if all(isinstance(x, str) for x in l):
	lst_type = 'the list you entered is of sting type'
	for x in l:
		newStr = newStr + ' ' + x
	print lst_type
	print newStr
elif all(isinstance(x, int) for x in l):
	lst_type = 'the list you entered is of integer type'
	for x in l:
		total += x
	print lst_type
	print 'total: ' + str(total)
else:
	lst_type = 'the list you entered is of mixed type'
	for x in l:
		if isinstance(x, str):
			newStr = newStr + ' ' + x
		elif isinstance(float(x), float):
			total += x
	print lst_type
	print newStr
	print 'total: ' + str(total)