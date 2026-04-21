from random import randint
from util import input_while

def parse_wanted(s: str) -> tuple[int, bool]:
    n: int
    try:
        n = int(s)
    except ValueError:
        print(f'{s} is not a valid integer')
        return 0, False
    
    if n < 1 or n > 6:
        print('the number must be between 1 and 6')
        return 0, False
    
    return n, True

def main() -> None:
    wanted_num: int = input_while('want> ', parse_wanted)

    tries = 0
    while True:
        k1 = randint(1, 6)
        k2 = randint(1, 6)

        print(f'{tries + 1}: {k1} x {k2}')

        if k1 == k2 and k1 == wanted_num:
            print(f'{k1} matches after {tries} tries')
            break

        tries += 1

if __name__ == '__main__':
    try: main()
    except KeyboardInterrupt: print('\nreceived sigint, exitting...')