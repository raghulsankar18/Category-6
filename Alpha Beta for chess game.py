# Category 6: Adversarial Search
# 2. Alpha-Beta Pruning for Chess Game

def alpha_beta(depth, node, alpha, beta, maximizing_player):

    if depth == 0:
        return node

    if maximizing_player:

        best_value = float("-inf")

        for child in node:

            value = alpha_beta(
                depth - 1,
                child,
                alpha,
                beta,
                False
            )

            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            if alpha >= beta:
                print("Branch pruned")
                break

        return best_value

    else:

        best_value = float("inf")

        for child in node:

            value = alpha_beta(
                depth - 1,
                child,
                alpha,
                beta,
                True
            )

            best_value = min(best_value, value)
            beta = min(beta, best_value)

            if alpha >= beta:
                print("Branch pruned")
                break

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
print("   ALPHA-BETA FOR CHESS GAME")
print("================================")

alpha = float("-inf")
beta = float("inf")

best_value = alpha_beta(
    3,
    game_tree,
    alpha,
    beta,
    True
)

print("\nBest evaluation value:", best_value)
print("Alpha-Beta pruning avoids unnecessary searches.")
