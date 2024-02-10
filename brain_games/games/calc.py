from random import randint
from random import choice


def calc():
    num1 = randint(1, 99)
    operator = choice(['*', '+', '-'])
    match operator:
        case "*":
            num2 = randint(1, 10)
            contr = num1 * num2
        case "+":
            num2 = randint(1, 99)
            contr = num1 + num2
        case "-":
            num2 = randint(1, num1)
            contr = num1 - num2
    question = str(num1) + str(operator) + str(num2)
    return question, str(contr)
