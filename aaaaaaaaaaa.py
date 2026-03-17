from random import randint

print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

while True:
    choice = input('> ')

    if choice == '1':
        print('1')
    elif choice == '2':
        KOD = randint(1, 10)
        kod = int(input('kod> '))
        if kod == KOD:
            break
        print('wrong')
    elif choice == '3':
        print('3')
    elif choice == '4':
        print('4')
    else:
        print('neeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')