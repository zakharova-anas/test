name = input(" Введите ваше имя : ")


def hello():
    print("-------------")
    print(" Привет, ", name, "!")
    print(" Это игра ")
    print(" крестики - нолики! ")
    print(" Формат ввода: x-пробел-y")
    print(" x - номер строки ")
    print(" y - номер столбца ")


def sq_field():  # отображение таблички поля
    print(f"  0 1 2")
    for i in range(3):
        row_sq = " ".join(field[i])
        print(f"{i} {row_sq}")
    print()


def ask():  # функция для запроса инф-ции у пользователя
    while True:
        coord = input("Ваш ход : ").split()

        if len(coord) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = coord

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне допустимого диапазона")
            continue

        if field[x][y] != " ":
            print("Клетка занята другим пользователем")
            continue

        return x, y


def win_check():  # выигрышная комбинация
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Х!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Х!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True

    for i in range(3):
        symbols = []
        symbols.append(field[i][i])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Х!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True

    for i in range(3):
        symbols = []
        symbols.append(field[i][2 - i])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Х!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True
    return False


hello()
field = [[" "] * 3 for i in range(3)]  # сам список поля
numbers = 0  # чтобы понимать, какой пользователь ходит
while True:
    numbers += 1

    sq_field()

    if numbers % 2 == 1:
        print("Ход крестика")
    else:
        print("Ходит нолик")

    x, y = ask()
    if numbers % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win_check():
        break

    if numbers == 9:
        print("Ничья")
        break
