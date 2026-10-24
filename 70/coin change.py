def coin_change(coins,amount):
    dp=[float("inf")]*(amount+1)
    dp[0]=0
    for a in range(1,amount+1):
        for coin in coins:
            if coin<=a:
                dp[a]=min(dp[a],1+dp[a-coin])
    return dp[amount] if dp[amount]!=float("inf") else -1
print(coin_change([1,3,4],6))