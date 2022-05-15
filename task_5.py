proceeds = int(input('Введите значение выручки фирмы: '))
costs = int(input('Введите значение издержек фирмы: '))

if proceeds > costs:
    profit = proceeds - costs

    print(f'Прибыль: { profit }')
    print(f'Рентабельность выручки: { profit / proceeds }')

    number_of_employees = int(input('Введите численность сотрудников: '))

    print(f'Прибыль фирмы в расчёте на одного сотрудника { profit / number_of_employees }')
elif proceeds < costs:
    print(f'Убыток: { costs - proceeds }')
else:
    print('Нет прибыли и нет убытков')
