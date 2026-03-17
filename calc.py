def calc():
    ops = {
        '+': lambda: str(lhs + rhs),
        '-': lambda: str(lhs - rhs),
        '*': lambda: str(lhs * rhs),
        '/': lambda: str(lhs / rhs if rhs != 0 else 'undefined'),
    }

    lhs = float(input('lhs> '))
    op = input('op> ')
    if not op in ops:
        print(f'invalid operation: {op}')
        return
    rhs = float(input('rhs> '))
    print(f'{lhs} {op} {rhs} = {ops[op]()}')

def main():
    while True:
        calc()
        do_quit = input('Quit? (y/N) ')
        if do_quit in ['y', 'Y']:
            break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\ninterrupted, exitting...')