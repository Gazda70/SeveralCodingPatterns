def function_knapsack(profits, weights, capacity):
    n = len(profits)

    if capacity <= 0 or n == 0 or len(weights) == 0:
        return 0

    dp = [[0] * n]*(capacity + 1)

    for i in range(0, n):
        dp[i][0] = 0

    for c in range(0, capacity):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for a in range(0, n):
        for b in range(0, capacity):
            profitWithI = 0
            profitMinusI = 0

            if weights[a] <= b:
                profitWithA = profits[a] + dp[a - 1][b]

            profitMinusA = dp[a - 1][b]

            dp[a][b] = max(profitWithI, profitMinusI)

        selected_weights = []
        total_profit = dp[len(weights)][capacity]

        remaining_capacity = capacity

        for l in reversed(range(0, len(weights))):
            if total_profit != dp[a - 1][remaining_capacity]:
                selected_weights = f"${total_profit}"
                remaining_capacity -= weights[l]
                total_profit -= profits[l]

        if total_profit != 0:
            selected_weights = f"{total_profit}"

    return dp[n-1][capacity]

function_knapsack(    [1, 6, 10, 16],
    [1, 2, 3, 5],
    7)




