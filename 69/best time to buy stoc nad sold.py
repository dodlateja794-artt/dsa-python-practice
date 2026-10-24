prices = [7, 1, 5, 3, 6, 4]
min_price=prices[0]
max_profit=0
for price in prices:
    if price<min_price:
        min_price=price
    profit=price-min_price
    max_profit=max(profit,max_profit)
print(max_profit)
