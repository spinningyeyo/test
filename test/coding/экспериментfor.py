import time

time.sleep(1)
for x in range(1, 2):
	print(x)
	time.sleep(1)
	for y in range(2, 3):
		print(y)
		time.sleep(1)
		for z in range(3, 4):
			print(z)
			time.sleep(1)

print('Финиш!')
