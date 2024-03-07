from random import choice


def prime():
    prime_list = [2]
    no_prime_list = []
    for prime_number in range(3, 150):
        i = 0
        while i <= len(prime_list) - 1:
            check = prime_number % prime_list[i] != 0
            i += 1
            if not check:
                no_prime_list.append(prime_number)
                break
        if check:
            prime_list.append(prime_number)
    contr = choice(('yes', 'no'))
    question = choice(prime_list) if contr == 'yes' else choice(no_prime_list)
    return question, str(contr)
