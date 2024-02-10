from random import randint


def even():
    random_num = randint(1, 99)
    if random_num % 2 == 0:
        contr = 'yes'
    else:
        contr = 'no'
    return random_num, contr
