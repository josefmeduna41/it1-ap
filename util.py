def input_while(query: str, transform):
    while True:
        inpt = input(query)
        val, ok = transform(inpt)

        if ok:
            return val