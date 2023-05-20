#!/usr/bin/python3
"""Module used to add two arrays."""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed for each total
    dp = [float('inf')] * (total + 1)

    # There are 0 coins needed to make a total of 0
    dp[0] = 0

    # Iterate through all totals from 1 to the target total
    for i in range(1, total + 1):
        # Try using each coin value to make the current total
        for coin in coins:
            if coin <= i:
                # If using this coin reduces the total number of coins needed, update the minimum
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still float('inf'), it means the total cannot be met by any number of coins
    if dp[total] == float('inf'):
        return -1

    return dp[total]
