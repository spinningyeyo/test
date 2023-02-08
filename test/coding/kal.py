# Калькулятор version 1.0

from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print( Fore.RED )
print( Back.YELLOW )

what = input( "Что надо сделать?  (+, - ): " )

print( Fore.RED )
print( Back.GREEN)

a = float( input("Введи первое число: ") )
b = float( input("Введи второе число: ") )

print( Fore.YELLOW )
print( Back.CYAN )

if what == "+":
    c = a + b
    print( "Результат: " + str(c))
elif what == "-":
    c = a - b
    print( "Результат: " + str(c))
else:
    print("Выбран неверная операция!")
    
input() 

c = 1
c += 1
print(c)

    


    