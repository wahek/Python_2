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

# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.
n = int(input('Введите число n: '))
i = 1
my_list = []
while i <= n:
    my_list.append((1 + 1 / i) ** i)
    i += 1
my_sum = 0
for i in my_list:
    my_sum += i
print(my_list)
print(f'Сумма элементов = {my_sum}')