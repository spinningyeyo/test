x = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя,.!?'
y = input('Введите тексте:\n')

for i in x:
	count = 0
	for r in y:
		if i == r:
			count += 1

	if count > 0:
			print('Букв или знаков', i, 'было', count)