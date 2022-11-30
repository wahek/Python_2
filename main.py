# number = input('Введите вещественное число: ')
# my_list = []
# my_sum = 0
# for i in number:
#     my_list.append(i)
# for i in my_list:
#     if i == ',':
#         my_list.remove(',')
#     elif i == '.':
#         my_list.remove('.')
# for i in my_list:
#     my_sum += int(i)
# print(my_sum)
import random

# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.
# n = int(input('Введите число n: '))
# i = 1
# my_list = []
# while i <= n:
#     my_list.append((1 + 1 / i) ** i)
#     i += 1
# my_sum = 0
# for i in my_list:
#     my_sum += i
# print(my_list)
# print(f'Сумма элементов = {my_sum}')

# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
my_list = []
i = 0
while i < random.randint(10, 20):
    my_list.append(random.randint(1, 100))
    i += 1
print(my_list)
for i in range(len(my_list)):
    j = random.randrange(len(my_list))
    temp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = temp
print(my_list)
# ДОПОЛНИТЕЛЬНО, НО НЕОБЯЗАТЕЛЬНО:
# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

# my_list = []
# i = 0
# while i < random.randint(5, 10):
#     my_list.append(random.randint(1000, 10000))
#     i += 1
# print(my_list)
# number = int(input('Введите цифру для удаления: '))
# for item in my_list:
#     for i in range(item):
#         if i == number:
#             item.remove(number)
# print(my_list)