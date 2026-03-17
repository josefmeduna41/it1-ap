x: float
x = input('>')
for i in range(10):
    while True:
        try:
            n = float(input(f'{i}> '))
            break
        except ValueError:
            continue
    if not chosen:
        x = n
print(x)                                                                                                                                                                                                                                                                                                                                                                                                                                                                               