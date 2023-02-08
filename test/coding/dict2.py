d1 = {'a': 7, 'b': 9}
d2 = dict([[1,2], [3,4], [5,6]])
d3 = dict.fromkeys([1,2,3,4,5], 'value')



#d5 = d1.copy
#print(d1.items())
#print(d1.keys())
#print(d1.values())
#d1.update(d2)
#print(d1)

if 'c' in d1:
    d1['c']

y = d1.get('c', 'value')
print(y)

t = d1.pop('a')
print(t, d1)