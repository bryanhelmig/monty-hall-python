from random import SystemRandom

doors_count = 3
doors = set(range(doors_count))

rand = SystemRandom()


def set_choice(_set):
    return rand.choice(list(_set))


def monty_hall(chosen_door, switch_door=False):
    actual_door = set_choice(doors)

    revealed_door = set_choice(doors - {chosen_door, actual_door})

    if switch_door:
        chosen_door = next(iter(doors - {chosen_door, revealed_door}))

    return actual_door == chosen_door


if __name__ == '__main__':
    iterations = 100000

    switch_wins = 0
    no_switch_wins = 0

    for _ in range(iterations):
        if monty_hall(set_choice(doors), switch_door=True):
            switch_wins += 1
        if monty_hall(set_choice(doors), switch_door=False):
            no_switch_wins += 1

    print('{} out of {} wins ({}%) if you switch'.format(
        switch_wins, iterations, (switch_wins / iterations) * 100))
    print('{} out of {} wins ({}%) if you do not switch'.format(
        no_switch_wins, iterations, (no_switch_wins / iterations) * 100))
