x = ''

while len(x) < 5:
	y = input('enter the letter: ')
	if y == 'o':
		continue
	if y == 'l':
		break


	x += y

else:
	print(x)
	