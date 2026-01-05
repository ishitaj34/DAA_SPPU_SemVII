def fractional_knapsack(weights, profits, capacity):
    n = len(weights)

    ratio = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(n)]

    ratio.sort(reverse=True)

    total_profit = 0
    current_capacity = capacity

    print("Item\tWeight\tProfit\tTaken")

    for r, w, p in ratio:
        if current_capacity == 0:
            break
        
        if w <= current_capacity:
            current_capacity -= w
            total_profit += p
            print(f"Full\t{w}\t{p}\t100%")
        else:
            fraction = current_capacity / w
            total_profit += p * fraction
            print(f"Part\t{w}\t{p}\t{round(fraction*100,2)}%")
            current_capacity = 0

    return total_profit

weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50

max_profit = fractional_knapsack(weights, profits, capacity)
print("\nMaximum Profit =", max_profit)

