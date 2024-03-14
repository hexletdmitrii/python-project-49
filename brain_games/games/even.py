from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game():
    random_num = randint(1, 99)
    if random_num % 2 == 0:
        contr = 'yes'
    else:
        contr = 'no'
    return random_num, contr
