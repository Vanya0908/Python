#создать 2 переменные типа String с разными значениями
p_1 = '5'
p_2 = '10'

#создать 4 переменных типа Integer с разными значениями
p_3 = 2
p_4 = 4
p_5 = 6
p_6 = 8

#создать 3 переменных тира Float
p_7 = 1.2
p_8 = 2.2
p_9 = 3.2

#реализовать 15 вариантов сравнения Integer переменных с операторами >,<,>=,<=,!=.
print(p_4 > p_3)
print(p_5 > p_4)
print(p_6 > p_5)
print(p_3 < p_4)
print(p_4 < p_5)
print(p_5 < p_6)
print(p_4 >= p_3)
print(p_5 >= p_4)
print(p_6 >= p_5)
print(p_3 <= p_4)
print(p_4 <= p_5)
print(p_5 <= p_6)
print(p_3 != p_4)
print(p_4 != p_5)
print(p_5 != p_6)

#реализовать 9 вариантов сравнения Float переменных с операторами >,<,>=,<=,!=.
print(p_8 > p_7)
print(p_9 > p_8)
print(p_7 < p_8)
print(p_8 < p_9)
print(p_8 >= p_7)
print(p_9 >= p_8)
print(p_7 <= p_8)
print(p_8 <= p_9)
print(p_8 != p_9)

#реализовать 10 вариантов сравнения Integer переменных с операторами >,<,>=,<=,!= и условными выражениями(end,or,not)
result = p_4 > p_3 and p_5 > p_4
print(result)
result = p_6 > p_5 and p_4 > p_3
print(result)
result = p_3 < p_4 and p_5 < p_6
print(result)
result = p_5 < p_6 and p_3 < p_4
print(result)
result = p_4 >= p_3 or p_5 <= p_4
print(result)
result = p_6 <= p_5 or p_4 >= p_3
print(result)
result = not p_3 >= p_4
print(result)
result = not p_4 <= p_3
print(result)
result = not p_4 != p_3
print(result)
result = not p_4 != p_5
print(result)

#сделать скрипт используя функцию input()
#функция должна на вход принимать цeлое число
#выводить должна "вы ввели число =(введенное число)которое(меньше/больше/равно)30"
print('введите a =')
a = int(input())
if a < 30:
    print('a < 30')
elif a > 30:
    print('a > 30')
else:
    print('a =30')

#cделать скрипт используя функцию input()
#функция должна на вход принимать целое число
#внутри функции должно сгенерироваться рандомное целое число
#выводить должна"вы ввели число =(введенное число)которое(меньше/больше/равно)сгенерированному числу"

import random
print('введите b =')
b = int(input())
n_1 = random.randint(1,100)
print(random.randint(1,100))
if  b < n_1:
    print('b < n_1')
elif b > 20:
    print('b > n_1')
else:
    print('b = n_1')

#сделать скрипт используя функцию input()
#функция должна на вход принимать целое число
#внутри функции должно сгенерироваться два целых числа
#выводить должна "вы ввели число=(введенное число)которое(меньше/больше/равно и меньше/равно)сгенертрованному числу"
print('введите c =')
c = int(input())
n_2 = random.randint(1,100)
print(random.randint(1,100))

if c < n_2:
    print('c < n_2')
elif c > n_2:
    print('c > n_2')
else:
    print('c =< n_2')

n_3 = random.randint(1,100)
print(random.randint(1,100))

if c < n_3:
    print('c < n_3')
elif c > n_3:
    print('c > n_3')
else:
    print('c =< n_3')
    