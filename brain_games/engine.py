from brain_games.cli import welcome_user
from brain_games.games.calc import calc
from brain_games.games.even import even
from brain_games.games.gcd import find_gcd
from brain_games.games.progression import progres


def engine(game, text):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    print(text)
    for i in range(3):
        match game:
            case 'calc':
                (question, contr) = calc()
            case 'even':
                (question, contr) = even()
            case 'gcd':
                (question, contr) = find_gcd()
            case 'progression':
                (question, contr) = progres()
        print(f'Question: {question}')
        ans = input('Your answer: ')
        if ans.lower() != contr:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{contr}'.")
            print(f"Let's try again, {name}!")
            return
    return print(f'Congratulations, {name}!')
