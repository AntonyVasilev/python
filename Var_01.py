# Задание 1

my_int = 5
my_bool = True
my_float = 2.5687
my_str = 'test'
my_list = [9, 'test1', 3.3]
my_tuple = (9, 'test1', 3.3)
my_dict = {'name': 'Anton', 'city': 'Moscow'}

print(my_int + 14)
print(not my_bool)
print(my_float + my_int)
print(my_str + my_str)
print(my_list)
print(my_tuple)
print(my_dict)
print(f'{my_int} = 5: {my_bool}')

user_int = int(input('Введите целое число: '))
user_str = input('Введите текст: ')

i = 0
while i < user_int:
    print(user_str)
    i += 1
