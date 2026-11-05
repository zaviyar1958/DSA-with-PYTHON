prices = list(map(int, input("Enter prices : ").split()))
min_price = float("inf")
max_profit = 0
n = len(prices)
for i in range (0, n) :
    min_price = min(min_price, prices[i])
    max_profit = max(max_profit, prices[i] - min_price)
print("Maximum profit is : ", max_profit)