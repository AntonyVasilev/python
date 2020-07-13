# Задание 5

revenue = float(input('Введите размер выручки компании: '))
costs = float(input('Введите размер издержек компании: '))

if revenue > costs:
    profit = True
    print('Ваша финансовая деятельность прибыльна.')
else:
    profit = False
    print('Ваша финансовая деятельность убыточна.')

if profit:
    income = revenue - costs  # Расчет прибыли
    profitability = income / revenue  # Расчет рентебельности
    print(f'Рентабельность выручки: {profitability:.02%}')
    staff = int(input('Введите количество сотрудников вашей компании: '))
    staff_income = income / staff
    print(f'Прибыль в расчете на одного сотрудника: {staff_income:.02f}')
