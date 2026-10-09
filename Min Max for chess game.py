# Category 6: Adversarial Search
# 1. Min-Max Search Algorithm for Chess Game

def minimax(depth, node, maximizing_player):

    if depth == 0:
        return node

    if maximizing_player:
        best_value = float("-inf")

        for child in node:
            value = minimax(depth - 1, child, False)
            best_value = max(best_value, value)

        return best_value

    else:
        best_value = float("inf")

        for child in node:
            value = minimax(depth - 1, child, True)
            best_value = min(best_value, value)

        return best_value


game_tree = [
    [
        [3, 5],
        [2, 9]
    ],
    [
        [12, 5],
        [4, 7]
    ]
]

print("================================")
print("   MIN-MAX FOR CHESS GAME")
print("================================")

best_move = minimax(3, game_tree, True)

print("\nBest evaluation value:", best_move)
print("MAX chooses the move with the highest value.")
