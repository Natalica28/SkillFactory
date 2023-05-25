def field_print():
    print(" ", 0, 1, 2)
    for i in range(3):
        print(i, field[i][0], field[i][1], field[i][2])
    print("Чтобы походить, введите координаты строки и столбца")

def check_input():
    while True:
        x = input("Введите координату строки: ")
        y = input("Введите координату столбца: ")

        if len(x) != 1 or len(y) != 1\
        or not (x.isdigit()) or not (y.isdigit()):
            print("Некорректные координаты")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2 \
        or x is None or y is None:
            print("Некорректные координаты")
            continue

        return x, y


def winner():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for i in win_cord:
        symbols = []
        for j in i:
            symbols.append(field[j[0]][j[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл ИГРОК 1!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл ИГРОК 2!")
            return True
    return False

field = [["-"] * 3 for i in range(3)]

count = 0
while True:
    count += 1
    field_print()
    if count % 2 == 1:
        print("ХОД ИГРОКА 1")
    else:
        print("ХОД ИГРОКА 2")

    x, y = check_input()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if winner():
        break

    if count == 9:
        print(" Ничья!")
        break