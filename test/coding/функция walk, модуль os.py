import os
import time

#('C:\\Users\\yuten\\Desktop\\папка для опытов', ['папка 1', 'папка 2'], ['файл 1.txt', 'файл 2.txt', 'фотка.jpg'])

x = []

for adress, dirs, files in os.walk('C:\\Users\yuten\Desktop\папка для опытов'):
    for file in files:
        full = os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 86400:
            x.append(full)

print(x)

    
