#1.

my_list = [0] * 98
my_list.insert(0, 1)
my_list.append(1)
print(my_list)


#2.

even_list = []
num = 2
while len(even_list) < 50:
    even_list.append(num)
    num += 2
print(even_list)


#3.

import random

my_list = [random.randint(1, 10) for _ in range(10)]
print(my_list)

x = int(input("Введите число: "))
if x in my_list:
    print("Номер элемента:", my_list.index(x))
else:
    print("-1")


#4.

import random

my_list = [random.randint(1, 10) for _ in range(10)]
print(my_list)

sum_list = sum(my_list)
prod_list = 1
for num in my_list:
    prod_list *= num

print("Сумма элементов:", sum_list)
print("Произведение элементов:", prod_list)


#5.

import random

my_list = [random.randint(1, 100) for _ in range(10)]
print(my_list)

max_num = max(my_list)
print("Наибольший элемент:", max_num)


#6.

import random

my_list = [random.randint(1, 5) for _ in range(10)]
print(my_list)

duplicates = set([num for num in my_list if my_list.count(num) > 1])
if duplicates:
    print("Повторяющиеся элементы:", duplicates)
else:
    print("Повторяющихся элементов нет")


#7.

import random

my_list = [random.randint(1, 100) for _ in range(10)]
print(my_list)

max_num = max(my_list)
min_num = min(my_list)
max_index = my_list.index(max_num)
min_index = my_list.index(min_num)

my_list[max_index], my_list[min_index] = my_list[min_index], my_list[max_index]
print("Измененный список:", my_list)


#8.

n = int(input("Введите количество чисел: "))
my_list = [int(input("Введите число: ")) for i in range(n)]
print("Исходный список:", my_list)

new_list = my_list[::2]
print("Список без элементов на нечетных индексах:", new_list)


#9.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_list = list(set(a) & set(b))
print(common_list)
