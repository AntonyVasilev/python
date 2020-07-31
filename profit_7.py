# Task 7
"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее
в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

average_profit = 0
num_workers = 0
companies = {}
average_dict = {}

with open('companies_info.txt', encoding='utf-8') as f:
    for line in f:
        name, comp_type, incom, costs = line.split()
        # print(name, comp_type, incom, costs)
        fin_result = float(incom) - float(costs)
        if fin_result >= 0:
            average_profit += fin_result
            num_workers += 1
        companies[name] = round(fin_result, 2)

average_dict['average_profit'] = round(average_profit / num_workers, 2)
companies_list = [companies, average_dict]
print(companies_list)

with open('companies.json', 'w', encoding='utf-8') as f:
    json.dump(companies_list, f)
