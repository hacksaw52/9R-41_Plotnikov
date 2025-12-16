def print_board(board):
    print("\n" + " " * 4 + "Игровое поле")
    print("   ┌───┬───┬───┐")
    print("   │ 0 │ 1 │ 2 │")
    print("   ├───┼───┼───┤")

    for i in range(3):
        row_str = f" {i} │"
        for j in range(3):
            symbol = " " if board[i][j] == "-" else board[i][j]
            row_str += f" {symbol} │"
        print(row_str)
        if i < 2:
            print("   ├───┼───┼───┤")

    print("   └───┴───┴───┘")


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '-':
            return board[i][0]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != '-':
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return None

    return 'Ничья'


def is_valid_move(board, row, col):
    if row < 0 or row > 2:
        return False
    if col < 0 or col > 2:
        return False
    if board[row][col] != '-':
        return False
    return True


def get_player_move():
    while True:
        try:
            cords = input("Введите координаты (строка столбец): ")
            parts = cords.split()

            if len(parts) != 2:
                print("Ошибка! Нужно две цифры через пробел")
                continue

            row = int(parts[0])
            col = int(parts[1])

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Ошибка! Цифры должны быть от 0 до 2")
                continue

            return row, col

        except ValueError:
            print("Ошибка! Введите цифры от 0 до 2")


def main():
    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]

    current_player = 'X'
    game_over = False

    print("\n" + "=" * 35)
    print("      Игра: Крестики-Нолики")
    print("=" * 35)
    print("Правила:")
    print("1. Игроки по очереди ставят X и O")
    print("2. Ход: строка столбец (например: 0 1)")
    print("=" * 35)

    while not game_over:
        print_board(board)
        print(f"\nХодит игрок: {current_player}")

        while True:
            row, col = get_player_move()
            if is_valid_move(board, row, col):
                break
            else:
                print("Эта клетка уже занята!")

        board[row][col] = current_player

        result = check_winner(board)

        if result is not None:
            print_board(board)
            print("\n" + "=" * 30)
            print(" " * 9 + "Конец игры!")
            if result == 'Ничья':
                print(" " * 12 + "Ничья!")
            else:
                print(" " * 7 + f"Победил игрок {result}!")
            print("=" * 30)
            game_over = True
        else:
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'


main()