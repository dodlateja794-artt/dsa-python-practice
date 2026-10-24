prices = [7, 1, 5, 3, 6, 4]
min_price=prices[0]
max_profit=0
for i in prices:
    if i<min_price:
        min_price=i
    profit=i-min_price
    max_profit=max(profit,max_profit)
print(max_profit)
