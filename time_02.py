# Задание 2
# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_sec = int(input('Введите количество секунд: '))

hours = user_sec // 3600
# print(hours)
minutes = (user_sec - hours * 3600) // 60
# print(minutes)
seconds = user_sec % 60
# print(seconds)

# print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))
print(f'{hours:02}:{minutes:02}:{seconds:02}')
