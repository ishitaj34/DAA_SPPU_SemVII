def knapsack(weights, values, capacity):
    n = len(values)

    # Create DP table (n+1) x (capacity+1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:  # item can be included
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], 
                               dp[i - 1][w])
            else:  # item cannot be included
                dp[i][w] = dp[i - 1][w]

    # The last cell contains the maximum profit
    return dp[n][capacity]

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_profit = knapsack(weights, values, capacity)
print("Maximum profit:", max_profit)
