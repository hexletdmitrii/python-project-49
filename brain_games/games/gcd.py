from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_game():
    num1 = randint(1, 99)
    num2 = randint(1, 99)
    contr = gcd(num1, num2)
    question = f'{num1} {num2}'
    return question, str(contr)
