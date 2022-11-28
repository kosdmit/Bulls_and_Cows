import random



def make_number(digit_count):
    global number
    number = list()

    number.append(random.randint(1, 9))
    flag = 0
    for i in range(1, digit_count):

        while flag != len(number):
            flag = 0
            digit = random.randint(0, 9)
            for item in number:
                if digit != item:
                    flag += 1
        number.append(digit)

    return number


def check_number(user_number):
    bulls_count = 0
    cows_count = 0
    bulls_and_cows = {'bulls': bulls_count, 'cows': cows_count}
    for digit in user_number:
        if digit in number:
            bulls_and_cows['cows'] += 1
    for i in range(len(number)):
        if user_number[i] == number[i]:
            bulls_and_cows['bulls'] += 1
            bulls_and_cows['cows'] -= 1

    return bulls_and_cows
