 r = open('file.txt', 'a')
try:
    r.write('something' + '\n' )
    10/0
    r.write('что-то')
finally:
    r.close()

 print ('Всё норм')

#with open('file.txt', 'a') as r:
#	r.write('something' + '\n')
#    5/0
#	r.write('что-то')

#print('Всё норм')


