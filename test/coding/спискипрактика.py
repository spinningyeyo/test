n  = list(range(1, 21))
b = n[start:stop:step]
m = []

for i in n:
    if i  % 2 ==  0:
        m.append(i) 
        n.remove(i)
    

else:
    print(m)
    print(n) 

print(b)
 