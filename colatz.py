def input_while(query: str, transform):
    while True:
        inpt = input(query)
        val, ok = transform(inpt)

        if ok:
            return val

def colatz():
    def input_cond(x: str) -> tuple[int, bool]:
        try:
            ix = int(x)
            if ix <= 0:
                print('error: not a natural number')
                return 0, False
            return ix, True
        except ValueError:
            print('error: not an integer')
            return 0, False
    n = input_while('n> ', input_cond)

    print(f'starting with {n}')
    passes: int = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n *= 3
            n += 1
        print(f'pass={passes+1}, {n=}')
        passes += 1

    print(f'got 1 in {passes} passes')

if __name__ == '__main__':
    try:
        colatz()
    except KeyboardInterrupt:
        print('\ninterrupted, exitting...')