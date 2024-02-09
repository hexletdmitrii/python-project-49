from brain_games.cli import welcome_user
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        random_num = randint(1, 99)
        if random_num % 2 == 0:
            contr = 'yes'
        else:
            contr = 'no'
        print(f'Question: {random_num}')
        ans = input('Your answer: ')
        if ans.lower() != contr:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{contr}'.")
            print(f"Let's try again, {name}!")
            return
    return print(f'Congratulations, {name}!')
