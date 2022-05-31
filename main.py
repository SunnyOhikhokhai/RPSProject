import random


while True:
    make_a_pick = input('Enter a choice(R, P, S): ')
    possible_actions = ["R", "P", "S"]
    CPU = random.choice(possible_actions)

    print(f'Player {make_a_pick}, CPU {CPU}.')

    if make_a_pick == CPU:
        print(f'Both players selected {make_a_pick}. It is a tie!')
    elif make_a_pick == 'R':
        if CPU == 'S':
            print('Rock beats Scissors! You win')
        else:
            print('Paper beats Rock, You lose')
    elif make_a_pick == 'P':
        if CPU == 'R':
            print('Paper beats Rock, You win!')
        else:
            print('Scissors beats paper, You lose')
    elif make_a_pick == 'S':
        if CPU == 'P':
            print('Scissors beats paper, You win!')
        else:
            print('Rock beats scissors, You lose')
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

