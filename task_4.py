user_number = int(input('Enter natural number: '))

number = user_number

max_digit = number % 10
number = number // 10

while number:
    current_digit = number % 10
    number = number // 10

    if current_digit > max_digit:
        max_digit = current_digit

print(f'Max digit in number { user_number } is { max_digit }')
