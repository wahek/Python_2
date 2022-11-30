number = input('Введите вещественное число: ')
my_list = []
my_sum = 0
for i in number:
    my_list.append(i)
for i in my_list:
    if i == ',':
        my_list.remove(',')
    elif i == '.':
        my_list.remove('.')
for i in my_list:
    my_sum += int(i)
print(my_sum)
