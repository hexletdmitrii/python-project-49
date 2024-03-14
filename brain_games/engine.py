from brain_games.cli import welcome_user


def engine(game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    for i in range(3):
        (question, correct_answer) = game.generate_game()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer.lower() != correct_answer:
            answer = ' is wrong answer ;(. Correct answer was '
            print(f"'{user_answer}'" + answer + f"'{correct_answer}'" + '.')
            print(f"Let's try again, {name}!")
            return
    return print(f'Congratulations, {name}!')
