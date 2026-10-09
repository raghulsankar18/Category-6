# Category 6: Adversarial Search
# 3. Min-Max Search for Tic-Tac-Toe

board = [" "] * 9


def display_board():

    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner():

    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:

        if (
            board[a] != " "
            and board[a] == board[b]
            and board[b] == board[c]
        ):
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def minimax(is_ai_turn):

    result = check_winner()

    if result == "O":
        return 1

    if result == "X":
        return -1

    if result == "Draw":
        return 0

    if is_ai_turn:

        best_score = float("-inf")

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(
                    best_score,
                    score
                )

        return best_score

    else:

        best_score = float("inf")

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(
                    best_score,
                    score
                )

        return best_score


def find_best_move():

    best_score = float("-inf")
    best_move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:

                best_score = score
                best_move = i

    return best_move


print("================================")
print("     TIC-TAC-TOE USING MIN-MAX")
print("================================")

print("Positions are numbered from 1 to 9.")

print()
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")


while True:

    display_board()

    try:
        position = int(
            input("Enter your position (1-9): ")
        ) - 1

    except ValueError:
        print("Please enter a number.")
        continue

    if position < 0 or position > 8:
        print("Choose a position between 1 and 9.")
        continue

    if board[position] != " ":
        print("That position is already occupied.")
        continue

    board[position] = "X"

    result = check_winner()

    if result is not None:
        display_board()
        break

    ai_move = find_best_move()

    if ai_move is not None:
        board[ai_move] = "O"

    result = check_winner()

    if result is not None:
        display_board()
        break


if result == "X":
    print("You win!")

elif result == "O":
    print("AI wins!")

else:
    print("It's a draw!")
