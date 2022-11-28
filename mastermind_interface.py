import mastermind_engine as engine



digit_count = int(input('Сколько цифр загадать? Введите число: '))

engine.make_number(digit_count)

user_input = input(f'Угадайте, что загадал компьютер? Введите число из {digit_count} цифр: ')
user_number = list()
steps = 1
for digit in user_input:
    user_number.append(int(digit))
bulls_and_cows = engine.check_number(user_number)
while bulls_and_cows['bulls'] != digit_count:
    print(f"быки - {bulls_and_cows['bulls']}, коровы - {bulls_and_cows['cows']}")
    user_input = input(f'Введите новое число из {digit_count} цифр: ')
    user_number = list()
    for digit in user_input:
        user_number.append(int(digit))
    steps += 1
    bulls_and_cows = engine.check_number(user_number)

print('Вы отгадали число!')
print(f'Совершено {steps} ходов. Хотите еще партию?')
