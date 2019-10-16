def draw(width: int, height: int, symb: str):
    for i in range(width):
        print(symb, end='')
    print()

    for i in range(height - 2):
        print(symb, end='')

        for i in range(width - 2):
            print(' ', end='')

        print(symb)

    for i in range(width):
        print(symb, end='')


draw(int(input("ширина: ")), int(input("высота: ")), input("символ: "))