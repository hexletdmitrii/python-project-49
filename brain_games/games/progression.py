from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def generate_game():
    leng_progres = randint(5, 12)
    first_number = randint(1, 10)
    step_num = randint(2, 8)
    random_element = randint(1, leng_progres)
    question = ''
    i = 1
    while i <= leng_progres:
        if random_element == i:
            question = str(question) + '.. '
            contr = first_number
        else:
            question = question + str(first_number) + ' '
        first_number += step_num
        i += 1
    return question, str(contr)
