result_of_first_day = int(input('Введите результат первого дня: '))
number_of_km = int(input('Введите количество километров: '))

day = 1
result = result_of_first_day

while result < number_of_km:
    percentage = 0.1
    result += result * percentage
    day += 1

print(f'На { day }-ой день спортсмен достиг результата - не менее { number_of_km } км')
